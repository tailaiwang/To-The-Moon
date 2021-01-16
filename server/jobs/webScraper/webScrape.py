import praw
import pandas as pd
import datetime as dt
from praw.models import MoreComments
from praw.reddit import Subreddit
import re
import json
import csv
import os


# convert to json
# json format
# {
#   "stockTicker":
#   "title":
#   "selfText": contents of post
#   "score":
#   "comments":
#   "linkFlairText":
#   "totalAwardsReceived":
# }


def getCommentConcatenated(submission):
    commentConcatenated = ""
    submission.comments.replace_more(limit=None)
    for comment in submission.comments.list():
        commentConcatenated += comment.body
    return commentConcatenated


def webScrapeToJSON():

    print("Connecting to Reddit API...")

    reddit = praw.Reddit(client_id='Yx811ChQuzwdCg',
                         client_secret='KPTiWELMRKl89hW85LY_l89qpchG7A',
                         user_agent='webScrapeReddit',
                         username='bill_cui57',
                         password='Happytime1')

    print("Connected!")
    print("Loading set of valid tickers from CSV...")

    tickerSet = set()
    script_dir = os.path.dirname(__file__)
    full_path = os.path.join(script_dir, 'assets/NYSE.csv')
    with open(full_path, newline='') as NYSEfile:
        reader = csv.reader(NYSEfile)
        for row in reader:
            tickerSet.add(row[0])

    script_dir = os.path.dirname(__file__)
    full_path = os.path.join(script_dir, 'assets/NASDAQ.csv')
    with open(full_path, newline='') as NASDAQfile:
        reader = csv.reader(NASDAQfile)
        for row in reader:
            tickerSet.add(row[0])

    print("Loaded!")

    targetSubReddit = "wallstreetbets"
    print("Currently targetting: r\\" + targetSubReddit)

    subreddit = reddit.subreddit(targetSubReddit)
    results = []

    def addSubmissionResults(submission):
        target = re.compile('[$][A-Za-z][\S]*')
        if re.match(target, submission.title):
            # could be a post that has a ticker (does this first to elimate unnecessary checks in set)
            candidate = target.search(submission.title).group()
            # the detected stock ticker without $
            candidateWithDollarSign = candidate[1:]
            if candidateWithDollarSign in tickerSet:
                # definitely a post that has ticker
                stockTicker = candidateWithDollarSign
                title = submission.title
                selfText = submission.selftext
                score = submission.score
                comments = getCommentConcatenated(submission)
                linkFlairText = submission.link_flair_text
                totalAwardsReceived = submission.total_awards_received

                result = {
                    "stockTicker": stockTicker,
                    "title": title,
                    "selfText": selfText,
                    "score": score,
                    "comment": comments,
                    "linkFlairText": linkFlairText,
                    "totalAwardsReceived": totalAwardsReceived
                }
                results.append(result)

    print("Scraping from controversial...")
    for submission in subreddit.controversial(limit=10000):
        addSubmissionResults(submission)
    print("Done!")
    print("Scraping from hot...")
    for submission in subreddit.hot(limit=10000):
        addSubmissionResults(submission)
    print("Done!")
    print("Scraping from new...")
    for submission in subreddit.new(limit=10000):
        addSubmissionResults(submission)
    print("Done!")
    print("Scraping from rising...")
    for submission in subreddit.rising(limit=10000):
        addSubmissionResults(submission)
    print("Done!")
    print("Scraping from top...")
    for submission in subreddit.top(limit=10000):
        addSubmissionResults(submission)
    print("Done!")
    print("Saving results to JSON")
    with open('scrapeResults.json', "w") as outfile:
        json.dump(results, outfile)
    print("Bye bye!")
