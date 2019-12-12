#Store all the possible friends in a list to revise
def search_friends(hashtags_number, users_number):
    friend_list = []

    for line in find_hashtags(hashtags_number):
        for user_id in iter(search_users_in_hashtag(line, users_number)):
            if user_id not in friend_list:
                friend_list.insert(-1, user_id)
    return friend_list
