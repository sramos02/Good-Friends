import tweepy
import friends

consumer_key = "###"
consumer_secret = "####"
access_token = "###"
access_token_secret = "###"

#######################################################################

# Creating the authentication object
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#######################################################################

# 1- Find user hashtags in timeline
def find_hashtags():
    used_hashtags = []

    print("Hashtags used:")
    for tweet in api.user_timeline(count=1000):
        # Dont know how many hashtags there are in the tweet, then read throught the end
        for w in tweet.text.split():
            if w.startswith('#'):
                while w.endswith('.'):  # Delete all points at the final of the hashtag
                    w = w[:-1]
                used_hashtags.insert(-1, w)
                print('\t' + w)

    print("############################")
    return used_hashtags


# 2- Look one by one and make a friend-list
def lookfor_comments(hashtag, count):
    lng = api.me().lang
    if lng is None:
        lng = "en"

    print("Tweets for " + hashtag)
    for tweet in tweepy.Cursor(api.search, q=hashtag, lang="en").items(count):
        print(tweet.text)


# 3- Make shorter list deleting "possible friends" that dont like the same themes than you
# 4- Make sure that the list dont descend to 0


#MAIN
#for line in find_hashtags():
for hash in find_hashtags():
   lookfor_comments("#Google", 3)
