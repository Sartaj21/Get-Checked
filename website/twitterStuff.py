import tweepy

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
    return tweet.data.text
#remove the tweet link at the end
def stripURL(text):
    delim = "https://"
    tmp = text.split(delim)
    if tmp[0] == "":
        return "tweet has no text"
    else:
        return tmp[0]



consumer_key = "4bckTJxx597EpwAgsVPB4jaZb" #api key
consumer_secret = "Gayo42TGGDFLz8ch6hPUJkY9Kjcv9KPi5kALDjcFoMMn30PlgS" #api key secret
access_token = "1558230505165824002-Vbimdu2lv7CyBHFuZYVbm8qb8lArVI"
access_token_secret = "PTPU5l7S3MydhTrcLXaoG52wvcwhExRF83u4NisDAtaBz"
bearer_token = "AAAAAAAAAAAAAAAAAAAAAPOdfwEAAAAAp498eSCHq4PudtLysRj0jSDFd2Q%3Dqs4lKuGovdEJxWehNIdFBF1qWqxHmyviIOiu60QXONgdo6LGtQ"

client = tweepy.Client(bearer_token)

tweet = getTweet("https://twitter.com/michaelreeves/status/1554203579652661248")
text = getTweetText(tweet)
norm = stripURL(text)
print(tweet)
print(text)
print(norm)