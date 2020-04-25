import requests
import numpy as np
import csv
import time
import datetime
start_time = time.time()



# def checker(username):
#     response = requests.get('https://api.vk.com/method/users.get?',
#                                 params={
#                                         'access_token': token,
#                                         'v': version,
#                                         'user_ids': username
#                                     }
#                                     )
#     try:
#         user = response.json()['response']
#     except:
#         return None
#     return True
def features(username):
    username = username.replace('id', '')
    if any(c.isalpha() for c in username):
        username = str(username)
    try:
        username = username.split('https://vk.com/')[1]
    except:
        username = username
    token = '681fa17e681fa17e681fa17ecc687118566681f681fa17e369ffd2b7c83b2960585ef73'
    version = '5.103'
    fields = [ " has_mobile, last_seen, connections, education, city, counters, has_photo,  fields, verified, personal, relatives, relation, schools, site, career, followers_count "]
    response = requests.get('https://api.vk.com/method/users.get?',
                                params={
                                        'access_token': token,
                                        'v': version,
                                        'user_ids': username
                                    }
                                    )
    try:
        user = response.json()['response']
    except:
        return "mistake"

    features = {}


    response = requests.get('https://api.vk.com/method/users.get?',
                            params={
                                    'access_token': token,
                                    'v': version,
                                    'user_ids': username,
                                    'fields': fields
                                }
                                )
    user = response.json()['response']

    try:
        banned = user[0]['deactivated']
    except:
        banned = None
    if banned:
        features = "banned"
        return features
    else:
        has_mobile = 0
        last_seen = 0
        links = 0
        education = 0
        city = 0
        has_photo = 0
        verified = 0
        personal = 0
        relatives = 0
        relation = 0
        closed = 1
        site = 0
        career = 0
        followers_count = 0
        closed = 0
        if user[0]['verified']:
            features = "verified"
            return features
        try:
            IsClosed = user[0]['is_closed']
        except:
            closed = 0
        if  IsClosed:
            try :
                has_photo = user['has_photo']
            except:
                has_photo = 0
            features = "private"
            return features
        else:   
            try:
                last_seen = user['last_seen']['time']
            except:
                last_seen = 0
            value = datetime.date.fromtimestamp(last_seen)
            today = datetime.date.today()
            diff = today - value
            diff.days
            try :
                instagram = user['instagram']
            except:
                instagram = None
            try :
                facebook = user['facebook']
            except:
                facebook = None
            try :
                twitter = user['twitter']
            except:
                twitter = None
            try :
                skype = user['skype']
            except:
                skype = None
            try :
                study = user['university_name']
            except:
                study = None
            try :
                school = user['schools']
            except:
                school = None
            try:
                verified = user['verified']
            except:
                verified = None
            try :
                has_photo = user['has_photo']
            except:
                has_photo = 0
            try :
                city = user['city']['title']
            except:
                city = None
            try:
                personal = user['personal']
            except:
                personal = None
            try:
                relation = user['relation']
            except:
                relation = None
            try:
                relatives = user['relatives']
            except:
                relatives = None
            try:
                site = user['site']
            except:
                site = None
            try:
                career = user['career']
            except:
                career = None
            try:
                followers_count = user[0]['followers_count']
            except:
                followers_count = 358
            try:
                user['can_access_closed']
            except:
                closed = 100
            if instagram or facebook or skype or twitter:
                links = 1
            else:
                links = 0
            if study or school:
                education = 1
            else:
                education = 0
            
            if personal or relation :
                personal = 1
            else:
                personal = 0
            if site :
                site = 1
            else:
                site = 0
            if career :
                career = 1
            else:
                career = 0
            if city:
                city = 1
            else:
                city = 0

            

            try :
                count_photos = user[0]['counters']['photos']
            except:
                count_photos = 0
            try :
                count_pages = user[0]['counters']['pages']
            except:
                count_pages = 0
            try :
                count_albums = user[0]['counters']['albums']
            except:
                count_albums = 0
            try :
                count_videos = user[0]['counters']['videos']
            except:
                count_videos = 0
            try :
                count_audios = user[0]['counters']['audios']
            except:
                count_audios = 0
            try :
                count_user_videos = user[0]['counters']['user_videos']
            except:
                count_user_videos = 0

            response = requests.get('https://api.vk.com/method/friends.get?',
            params={
                    'access_token': token,
                    'v': version,
                    'user_id': username
                }
                )
            try:
                count_user_friends = response.json()['response']['count']
            except:
                count_user_friends = 150
                

            # try :
            #     count_friends = count_user_friends['count']
            # except:
            #     count_friends = None







            features = {}

            features["IsCity"] = city
            features["IsProfile"] = personal
            features["IsLinks"] = links
            features["FriendCount"] = count_user_friends
            features["PhotoCount"] = count_photos
            features["PagesCount"] = count_pages
            features["FollowersCount"] = followers_count
            features["AlbumsCount"] = count_albums
            features["VideosCount"] = count_videos
            features["AudiosCount"] = count_audios
            features["OfflineDays"] = diff.days
            features["HasPhoto"] = has_photo
            features["Site"] = site
            features["Career"] = career
            features["Education"] = education


        try:
            features["following_followers_ratio"] = round(
                    count_user_friends / followers_count, 7)
        except ZeroDivisionError:
            features["following_followers_ratio"] = 2.8624688005235597

        # add following_users_ratio
        try:
            features["following_photos_ratio"] = round(
                    count_user_friends / count_photos, 7)
        except ZeroDivisionError:
            features["following_photos_ratio"] = 48.6537926973262

        # add followers_users_ratio
        try:
            features["followers_photos_ratio"] = round(
                followers_count / count_photos, 7)
        except ZeroDivisionError:
            features["followers_photos_ratio"] = 118.71968859411763
        return features
    # else:
    #     return Nonefe
