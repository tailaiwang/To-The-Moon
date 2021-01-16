import praw
import pandas as pd
import datetime as dt
from praw.models import MoreComments
from praw.reddit import Subreddit
import re
import json
import csv

reddit = praw.Reddit(client_id='Yx811ChQuzwdCg', \
                     client_secret='KPTiWELMRKl89hW85LY_l89qpchG7A', \
                     user_agent='webScrapeReddit', \
                     username='bill_cui57', \
                     password='Happytime1')


# url = "https://www.reddit.com/r/wallstreetbets/comments/ky3qg6/weekend_discussion_thread_for_the_weekend_of/"

# submission = reddit.submission(url=url)


# submission.comments.replace_more(limit=None)
# for top_level_comment in submission.comments:
#     print(top_level_comment.body)

tickerSet= set()
with open('NYSE.csv', newline='') as NYSEfile:
  reader = csv.reader(NYSEfile)
  for row in reader:
    tickerSet.add(row[0])

with open('NASDAQ.csv', newline='') as NASDAQfile:
  reader = csv.reader(NASDAQfile)
  for row in reader:
    tickerSet.add(row[0])


subreddit = reddit.subreddit("wallstreetbets")


results = []
#convert to json
#json format
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





for submission in subreddit.controversial(limit=10000):
  target = re.compile('[$][A-Za-z][\S]*')
  result = {}
  if re.match(target, submission.title):
      #could be a post that has a ticker (does this first to elimate unnecessary checks in set)
      candidate = target.search(submission.title).group()
      candidateWithDollarSign = candidate[1:] #the detected stock ticker without $
      if candidateWithDollarSign in tickerSet:
       #definitely a post that has ticker
        stockTicker = candidateWithDollarSign
        title = submission.title
        selfText = submission.selftext
        score = submission.score
        comments = getCommentConcatenated(submission)
        linkFlairText = submission.link_flair_text
        totalAwardsReceived = submission.total_awards_received


        result = {
          "stockTicker":stockTicker,
          "title": title,
          "selfText": selfText,
          "score": score,
          "comment": comments,
          "linkFlairText": linkFlairText,
          "totalAwardsReceived": totalAwardsReceived
        }
        results.append(result)



for submission in subreddit.hot(limit=10000):
  target = re.compile('[$][A-Za-z][\S]*')
  result = {}
  if re.match(target, submission.title):
      #could be a post that has a ticker (does this first to elimate unnecessary checks in set)
      candidate = target.search(submission.title).group()
      candidateWithDollarSign = candidate[1:] #the detected stock ticker without $
      if candidateWithDollarSign in tickerSet:
       #definitely a post that has ticker
        stockTicker = candidateWithDollarSign
        title = submission.title
        selfText = submission.selftext
        score = submission.score
        comments = getCommentConcatenated(submission)
        linkFlairText = submission.link_flair_text
        totalAwardsReceived = submission.total_awards_received


        result = {
          "stockTicker":stockTicker,
          "title": title,
          "selfText": selfText,
          "score": score,
          "comment": comments,
          "linkFlairText": linkFlairText,
          "totalAwardsReceived": totalAwardsReceived
        }
        results.append(result)



for submission in subreddit.new(limit=10000):
  target = re.compile('[$][A-Za-z][\S]*')
  result = {}
  if re.match(target, submission.title):
      #could be a post that has a ticker (does this first to elimate unnecessary checks in set)
      candidate = target.search(submission.title).group()
      candidateWithDollarSign = candidate[1:] #the detected stock ticker without $
      if candidateWithDollarSign in tickerSet:
       #definitely a post that has ticker
        stockTicker = candidateWithDollarSign
        title = submission.title
        selfText = submission.selftext
        score = submission.score
        comments = getCommentConcatenated(submission)
        linkFlairText = submission.link_flair_text
        totalAwardsReceived = submission.total_awards_received


        result = {
          "stockTicker":stockTicker,
          "title": title,
          "selfText": selfText,
          "score": score,
          "comment": comments,
          "linkFlairText": linkFlairText,
          "totalAwardsReceived": totalAwardsReceived
        }
        results.append(result)

for submission in subreddit.rising(limit=10000):
  target = re.compile('[$][A-Za-z][\S]*')
  result = {}
  if re.match(target, submission.title):
      #could be a post that has a ticker (does this first to elimate unnecessary checks in set)
      candidate = target.search(submission.title).group()
      candidateWithDollarSign = candidate[1:] #the detected stock ticker without $
      if candidateWithDollarSign in tickerSet:
       #definitely a post that has ticker
        stockTicker = candidateWithDollarSign
        title = submission.title
        selfText = submission.selftext
        score = submission.score
        comments = getCommentConcatenated(submission)
        linkFlairText = submission.link_flair_text
        totalAwardsReceived = submission.total_awards_received


        result = {
          "stockTicker":stockTicker,
          "title": title,
          "selfText": selfText,
          "score": score,
          "comment": comments,
          "linkFlairText": linkFlairText,
          "totalAwardsReceived": totalAwardsReceived
        }
        results.append(result)
        

for submission in subreddit.top(limit=10000):
  target = re.compile('[$][A-Za-z][\S]*')
  result = {}
  if re.match(target, submission.title):
      #could be a post that has a ticker (does this first to elimate unnecessary checks in set)
      candidate = target.search(submission.title).group()
      candidateWithDollarSign = candidate[1:] #the detected stock ticker without $
      if candidateWithDollarSign in tickerSet:
       #definitely a post that has ticker
        stockTicker = candidateWithDollarSign
        title = submission.title
        selfText = submission.selftext
        score = submission.score
        comments = getCommentConcatenated(submission)
        linkFlairText = submission.link_flair_text
        totalAwardsReceived = submission.total_awards_received


        result = {
          "stockTicker":stockTicker,
          "title": title,
          "selfText": selfText,
          "score": score,
          "comment": comments,
          "linkFlairText": linkFlairText,
          "totalAwardsReceived": totalAwardsReceived
        }
        results.append(result)


print(len(results))


with open("sample.json", "w") as outfile:  
    json.dump(results, outfile) 



    
