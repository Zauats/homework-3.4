from urllib.parse import urlencode
import json
from pip._vendor import requests

AUTH_URL = 'https://oauth.vk.com/authorize'
APP_ID = 6297716

url_data = {
    'client_id': APP_ID,
    'redirect_uri': 'https://oauth.vk.com/blank.html',
    'display': 'page',
    'scope': 'friends,status,video ',
    'response_type': "token",
    'v': '5.69'
}

print("?".join((AUTH_URL, urlencode(url_data))))

token = 'нужно ввести токен'
my_id = "ввести свой id"

params_for_friendsget = {
    "user_id": my_id,
    "order": "random",
}

def friend_id():
    response = requests.get('https://api.vk.com/method/friends.get', params_for_friendsget)
    friends_id = ""
    for friend_id in response.json()["response"]:
        friends_id += "," + str(friend_id)
    return friends_id


params_for_friendsgetMutual = {
    "access_token": token,
    'source_uid': my_id,
    "target_uids": friend_id(),
    "order": "random",
}

def mutual_friend():
    response = requests.get('https://api.vk.com/method/friends.getMutual', params_for_friendsgetMutual)

    for mutual_id_friends in response.json()["response"]:
        print("id друга: {}{}  ссылка на друга: {}{}".format(mutual_id_friends['id'], '\n',
            "https://vk.com/id" + str(mutual_id_friends["id"]), "\n"))

        for mutual_friend_id in mutual_id_friends["common_friends"]:
            print("  id общего друга: {} \n      ссылка на пользователя: {}".
                  format(mutual_friend_id,"https://vk.com/id" + str(mutual_friend_id)))
        print("\n"*2)
