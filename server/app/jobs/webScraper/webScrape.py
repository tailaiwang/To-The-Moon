import praw
import pandas as pd
import datetime as dt
from praw.models import MoreComments
from praw.reddit import Subreddit
import requests
import re
import json
import csv
import os
import math
from google.cloud import language_v1
from app import client


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


def webScrapeToJSONAndPush():

    print("Connecting to Reddit API...")

    reddit = praw.Reddit(client_id='Yx811ChQuzwdCg',
                         client_secret='INSERT_SECRET',
                         user_agent='webScrapeReddit',
                         username='INSERT_USERNAME',
                         password='INSERT_PASSWORD')

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

    # Calculates the average rating per stock ticker based on WSB

    def getSentiment(text):
        document = language_v1.Document(
            content=text, type_=language_v1.Document.Type.PLAIN_TEXT)

        # Detects the sentiment of the text
        sentiment = client.analyze_sentiment(
            request={'document': document}).document_sentiment
        return sentiment.score

    def calcRating(submission):
        rating = 0
        titleSenti = getSentiment(submission.title)
        descSenti = getSentiment(submission.selftext)
        commentsSenti = getSentiment(getCommentConcatenated(submission))
        totalSenti = (2 * titleSenti + 1.2 * descSenti + commentsSenti)/4.20

        # find the number of rocket ships inside the comments, title, desc
        target = re.compile('🚀')
        rocketShipCount = len(re.findall(target, submission.title + submission.selftext + getCommentConcatenated(submission)))
        # finds the number of YOLOs, each YOLO is +5
        yoloCount = str(submission.link_flair_text).count("YOLO")

        rating = (totalSenti * ( 1 + math.log(1 +submission.score,10)  + submission.total_awards_received
                                ) + math.log(1 +rocketShipCount) + yoloCount) 
        return rating

    

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
                id = submission.id
                rating = calcRating(submission)

                result = {
                    "id": id,
                    "stockTicker": stockTicker,
                    "title": title,
                    "selfText": selfText,
                    "score": score,
                    "comment": comments,
                    "linkFlairText": linkFlairText,
                    "totalAwardsReceived": totalAwardsReceived,
                    "rating": rating
                }
                results.append(result)
                print(result)





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
    script_dir = os.path.dirname(__file__)
    full_path = os.path.join(script_dir, 'scrapeResults.json')
    with open(full_path, "w") as outfile:
        json.dump(results, outfile)

    


    



    print("Bye bye!")
