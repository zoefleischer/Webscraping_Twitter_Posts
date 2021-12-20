# ----------------------AUTHENTICATION TO TWITTER API----------------

import tweepy

# Authenticate to Twitter
auth = tweepy.OAuthHandler("public_password", "private_password")
auth.set_access_token("public_token", "private_token")

# Create API object
api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

api = tweepy.API(auth, wait_on_rate_limit=True,
                 wait_on_rate_limit_notify=True)

# ----------------RETRIEVE COMMENTS WITHIN TWITTER'S ALLOWED RANGE (1week/3000tweets)------------

for tweet in tweepy.Cursor(api.search, q="#spacex",
                           lang="en",
                           since="2020-04-20", sleep_on_rate_limit=False).items():
    print(tweet.created_at, tweet.text)


# ----------------SURPASSING TWEET AMOUNT LIMIT (3000 TWEETS)--------------------

def tweets_to_df(searchQuery, language='', until):
    # If results from a specific ID onwards are reqd, set since_id to that ID.
    # else default to no lower limit, go as far back as API allows
    sinceId = None
    # If results only below a specific ID are, set max_id to that ID.
    # else default to no upper limit, start from the most recent tweet matching the search query.
    max_id = -1
    tweetCount = 0
    print("Downloading max {0} tweets".format(maxTweets))
    tweets = []
    while tweetCount < maxTweets:
        try:
            if (max_id <= 0):
                if (not sinceId):
                    new_tweets = api.search(q=searchQuery, count=100, lang=language, tweet_mode='extended')
                else:
                    new_tweets = api.search(q=searchQuery, count=100, lang=language, since_id=sinceId,
                                            tweet_mode='extended')
            else:
                if (not sinceId):
                    new_tweets = api.search(q=searchQuery, count=100, lang=language, tweet_mode='extended',
                                            max_id=str(max_id - 1))
                else:
                    new_tweets = api.search(q=searchQuery, count=100, lang=language, tweet_mode='extended',
                                            max_id=str(max_id - 1),
                                            since_id=sinceId)
            if not new_tweets:
                print("No more tweets found")
                break
            for tweet in new_tweets:
                tweets.append(tweet._json)
            tweetCount += len(new_tweets)
            print("Downloaded {0} tweets".format(tweetCount))
            max_id = new_tweets[-1].id
        except tweepy.TweepError as e:
            # Just exit if any error
            print("some error : " + str(e))
            break
    print("Downloaded {0} tweets".format(tweetCount))
    return pd.DataFrame(tweets)


def tweets_to_df(searchQuery="#spacex", language='en', until="2020-07-02")


tweets.to_csv("insert path")

# ---------------SURPASSING THE TIME LIMIT (1 WEEK BACK)-----------------------------

import GetOldTweets3 as got

tweetCriteria = got.manager.TweetCriteria().setQuerySearch("spacex") \
    .setSince("2020-06-02") \
    .setUntil("2020-07-01") \
 \
    tweets = got.manager.TweetManager.getTweets(tweetCriteria)
tweets

tweets.to_csv("insert path")

# ------------------EXTRACTING THE INFO FROM COMMENT OBJECT-----------


tweet_dates = [tweet.date for tweet in tweets]
tweet_dates_pd = pd.DataFrame(tweet_dates)
tweet_dates_pd.to_csv("insert path")

tweet_text = [tweet.text for tweet in tweets]
tweet_text_pd = pd.DataFrame(tweet_text)
tweet_text_pd.to_csv("insert path")

# ------------------------CHANGING DATE/TIME FORMAT----------------------

import pandas as pd

df = pd.read_csv("insert path")

df.columns = ['Index', 'Date']
df = df.drop("Index", 1)

date_list = [date.to_datetime for date in df['Date']]
# date_list.dt.strftime('%m/%d/%Y')

# separating date and time
df['Time'] = df['Date'].apply(lambda x: x[11:19])
df['Date'] = df['Date'].apply(lambda x: x[0:10])

df.to_csv("insert path")

# ------------COUNTING COMMENTS PER HOUR-----------

import pandas as pd

df = pd.read_csv("insert path", encoding="ISO-8859-2")

# turning the time into integers
df['Time'] = df['Time'].apply(lambda x: int(x[:2].replace(':', '.') if len(x) == 8 else int(x[:1].replace(':', '.'))))

# grouping by day and hour and counting comments for each hour
grouped = df.groupby(by=["Date", "Time"])['Comments'].count()

# saving it to PC
grouped_pd = pd.DataFrame(grouped)
grouped_pd.to_csv("insert path")

# -----------------------GETTING COMMENTS WITH SPECIFIC WORDS---------------

import pandas as pd

df = pd.read_csv("insert path", encoding="ISO-8859-2")
df.columns

pos_comm = []

for comment in df['0'][:7871]:
    print(comment)
    if type(comment) == str:
        if "amazing" in comment:
            pos_comm.append(comment)

pos_comm
len(pos_comm)