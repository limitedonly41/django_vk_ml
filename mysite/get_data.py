import aiohttp
import asyncio
import time
import requests
import time
import datetime
from aiohttp import ClientSession
start_time = time.time()

token = '18019db418019db418019db4a01875ed881180118019db447882228875fa30302b2b588'
version = '5.130'
fields = [" about, activities, books, career, city, connections, counters, country, education, followers_count, games, has_mobile, has_photo, interests, last_seen, military, occupation, personal, quotes, relation, relatives, site, universities, verified "]


def get_all_user_info(domain):
    domain = domain
    users_desc = []
    all_ids = []
    users_count = 0
    response = requests.get('https://api.vk.com/method/groups.getMembers?',
                            params={
                                'access_token': token,
                                'v': version,
                                'group_id': domain,
                                'count': 1
                            }
                            )

    count_items = response.json()['response']['count']
    print(count_items)

    async def get_ids(session, url):
        async with session.get(url) as resp:
            users = await resp.json()
            return users['response']['items']


    async def main():

        async with aiohttp.ClientSession() as session:

            tasks = []
            count = 100
            for offset in range(0, count_items, count):
                url = f'https://api.vk.com/method/groups.getMembers?access_token={token}&v={version}&group_id={domain}&count={count}&offset={offset}'
                tasks.append(asyncio.ensure_future(get_ids(session, url)))

            all_users = await asyncio.gather(*tasks)
            for user in all_users:
                all_ids.extend(user)

    asyncio.run(main())
    # print("--- %s seconds ---" % (time.time() - start_time))
    print("got: " ,len(all_ids))
    # print(all_ids[:150])

# commented 


    async def get_info(session, url, id):
        async with session.get(url) as resp:
            users = await resp.json()
            user = users['response']

            features = {}

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
                        has_photo = user[0]['has_photo']
                    except:
                        has_photo = 0
                    features = "private"
                    return features
                else:   
                    try:
                        last_seen = user[0]['last_seen']['time']
                    except:
                        last_seen = 0
                    value = datetime.date.fromtimestamp(last_seen)
                    today = datetime.date.today()
                    diff = today - value
                    diff.days
                    try :
                        instagram = user[0]['instagram']
                    except:
                        instagram = None
                    try :
                        facebook = user[0]['facebook']
                    except:
                        facebook = None
                    try :
                        twitter = user[0]['twitter']
                    except:
                        twitter = None
                    try :
                        skype = user[0]['skype']
                    except:
                        skype = None
                    try :
                        study = user[0]['university_name']
                    except:
                        study = None
                    try :
                        school = user[0]['schools']
                    except:
                        school = None
                    try:
                        verified = user[0]['verified']
                    except:
                        verified = None
                    try :
                        has_photo = user[0]['has_photo']
                    except:
                        has_photo = 0
                    try :
                        city = user[0]['city']['title']
                    except:
                        city = None
                    try:
                        personal = user[0]['personal']
                    except:
                        personal = None
                    try:
                        relation = user[0]['relation']
                    except:
                        relation = None
                    try:
                        relatives = user[0]['relatives']
                    except:
                        relatives = None
                    try:
                        site = user[0]['site']
                    except:
                        site = None
                    try:
                        career = user[0]['career']
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


                        

                    # try :
                    #     count_friends = count_user_friends['count']
                    # except:
                    #     count_friends = None







                    features = {}

                    features["IsCity"] = city
                    features["IsProfile"] = personal
                    features["IsLinks"] = links
                    
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

                # добавить соотношение друзья/подписчики
                # try:
                #     features["following_followers_ratio"] = round(
                #             count_user_friends / followers_count, 7)
                # except ZeroDivisionError:
                #     features["following_followers_ratio"] = 2.8624688005235597

                # добавить соотношение друзья/фото
                # try:
                #     features["following_photos_ratio"] = round(
                #             count_user_friends / count_photos, 7)
                # except ZeroDivisionError:
                #     features["following_photos_ratio"] = 48.6537926973262

                # # добавить соотношение подписчики/фото
                # try:
                #     features["followers_photos_ratio"] = round(
                #         followers_count / count_photos, 7)
                # except ZeroDivisionError:
                #     features["followers_photos_ratio"] = 118.71968859411763
                
        url_f = f'https://api.vk.com/method/friends.get?access_token={token}&v={version}&user_id={id}'
        async with session.get(url_f) as resp:
            users = await resp.json()
            try:
                count_user_friends = users['response']['count']
            except:
                count_user_friends = 150
            features["FriendCount"] = count_user_friends
            
            try:
                features["following_followers_ratio"] = round(
                        count_user_friends / followers_count, 7)
            except ZeroDivisionError:
                features["following_followers_ratio"] = 2.8624688005235597
            
            try:
                features["following_photos_ratio"] = round(
                        count_user_friends / count_photos, 7)
            except ZeroDivisionError:
                features["following_photos_ratio"] = 48.6537926973262

            # добавить соотношение подписчики/фото
            try:
                features["followers_photos_ratio"] = round(
                    followers_count / count_photos, 7)
            except ZeroDivisionError:
                features["followers_photos_ratio"] = 118.71968859411763
        return features

    all_ids_info = []

    fields = [ " has_mobile, last_seen, connections, education, city, counters, has_photo,  fields, verified, personal, relatives, relation, schools, site, career, followers_count "]

    async def main_info(all_ids):
        # if len(all_ids) > 50_000:
        #     for i in range(0, len(all_ids),50_000):
        #         if i + 50_000 > len(all_ids):
        #             ids = all_ids[i:]
        #         else:
        #             ids = all_ids[i:i+50_000]
        #         print("i")
        async with aiohttp.ClientSession() as session:

            tasks = []
            for id in all_ids:
                url = f'https://api.vk.com/method/users.get?access_token={token}&v={version}&user_ids={id}&fields={fields}'
                tasks.append(asyncio.ensure_future(get_info(session, url, id)))

            all_users_info = await asyncio.gather(*tasks)
            for user_info in all_users_info:
                all_ids_info.append(user_info)
    if len(all_ids) > 50_000:
        for i in range(0, len(all_ids),50_000):
            if i + 50_000 > len(all_ids):
                ids = all_ids[i:]
            else:
                ids = all_ids[i:i+50_000]
            print("i")

            asyncio.run(main_info(ids))
    else:
        asyncio.run(main_info(all_ids))

    # print(all_ids_info[:100])

    return all_ids_info


