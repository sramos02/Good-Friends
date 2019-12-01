# 1- Find hashtags in user timeline and return it
def find_hashtags(count):
    used_hashtags = []

    print("Hashtags used:")
    for tweet in api.user_timeline(count=count):
        # Dont know how many hashtags there are in the tweet, then read throught the end
        for w in tweet.text.split():
            if w.startswith('#'):
                while w.endswith('.'):  # Delete all points at the final of the hashtag
                    w = w[:-1]
                used_hashtags.insert(-1, w)
                print('\t' + w)

    print("############################")
    return used_hashtags
