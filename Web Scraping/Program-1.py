import tweepy
import emoji
import csv
import re

api = tweepy.Client(bearer_token = 'AAAAAAAAAAAAAAAAAAAAAPhAfwEAAAAAICqaz4qimZyFY0Fv4ypMJ22HMq0%3D7Zg0M4xOffFNAeje7plkpq6v1Y3v1nKSsYEnOGvTBSEc0a709v')

def search_tweets(query, max_results):
    tweets = api.search_recent_tweets(query = query + " -RT", max_results = max_results)
    return tweets

tweet = search_tweets('Manchester United', 10)

res = []
sentence = []
wor = []
data = []
for say in tweet.data:
  say.text = re.sub(',+', '', say.text)
  say.text = re.sub('-+', '', say.text)
  say.text = re.sub('@+','',say.text)
  say.text = re.sub('#[^\s]+', '',say.text)
  say.text = re.sub('http[^\s]+','URL',say.text)
  res.append(say.text.lower())

for twe in res:
    word = twe.split(' ')
    wor.append(word)
    word1 = twe.split('.')
    sentence.append(word1)

for a in wor:
    d1 = []
    for p in a:
        p = emoji.demojize(p)
        p = re.sub('_+', " ", p)
        d1.append(p)
    data.append(d1)

for b in sentence:
    d2 = []
    for k in b:
       k = emoji.demojize(k)
       k = re.sub('_+', " ", k)
       d2.append(k)
    data.append(d2)   

with open('tweets.csv', 'w', encoding ='UTF8', newline='') as f:
    writer = csv.writer(f)
    for row in data:
        writer.writerow(row)

