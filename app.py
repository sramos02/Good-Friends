import tweepy
import friends

consumer_key = "################################"
consumer_secret = "##################################"
access_token = "##########################################"
access_token_secret = "##############################"

#######################################################################

# Creating the authentication object
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#######################################################################

#1- Find user hashtags in timeline
used_hashtags = []
cont = 0

for tweet in api.user_timeline(count=3):
   if tweet.text.find('#'):
      # Dont know how many hashtags there are in the tweet, then read throught the end
      print(tweet.text)
      for w in tweet.text.split():
         if w.find('#'):
            used_hashtags.insert(-1, w)
   else: cont = cont + 1
print('Se han encontrado ' + str(cont) + ' tweets sin hashtags')

#2- Look one by one and make a friend-list
#3- Make shorter list deleting possible friend that no like the same x tweets
#4- Make sure that the list dont descend to 0
