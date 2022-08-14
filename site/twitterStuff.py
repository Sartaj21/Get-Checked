from flask import Flask, request, render_template

import tweepy
import datetime
import config
consumer_key = config.consumer_key
consumer_secret = config.consumer_secret #api key secret
access_token = config.access_token
access_token_secret = config.access_token_secret
bearer_token = config.bearer_token

client = tweepy.Client(bearer_token)

#move functions to a separate file later

#should just be the numbers after the URL
def getTweetID(url):
    return url.split("/")[-1]

#returns as int
#just do id_str for string
def getUserID(username):
    user = client.get_user(username = username)
    return user.data.id

def getTweet(url):
    return client.get_tweet(id = getTweetID(url))
def getTweetText(tweet):
    delim = "https://"
    #starts with a link
    if delim in tweet.data.text[:8]:
        return "tweet has no text"
    else:
        return tweet.data.text
#remove the tweet link at the end
def stripURL(text):
    delim = "https://"
    tmp = text.split(delim)
    if tmp[0] == "":
        return "tweet has no text"
    else:
        return tmp[0]
        

#format 1/1/2000
def formatDate(date):
    date = list(map(int, date.split("/")))
    return datetime.datetime(date[2], date[0], date[1])

#check if a tweet is real
#limited to most recent 3200 tweets
#give date as a string e.g (January 1st, 2000 is 1/1/2000)
def validate(username, text, date):
    userID = getUserID(username)
    text = text.lower()
    startTime = formatDate(date)
    endTime = startTime + datetime.timedelta(hours = 24)
    lis = client.get_users_tweets(id = userID, start_time = startTime, end_time = endTime).data
    if lis == None:
        return "no tweets found for that date"
    for tweet in lis:
        if stripURL(tweet.text).strip().lower() == text:
            return True
    return False

tweet = getTweet("https://twitter.com/michaelreeves/status/1551087064501862401")
text = getTweetText(tweet)
norm = stripURL(text)

app = Flask(__name__)

@app.route("/")

def my_form():
    return render_template("form.html")

print(tweet)
print(text)
print(norm)
print(validate("elonmusk", "Another orbital plane of polar satellites", "8/13/2022")) #testing purposes


