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

token = '3583f9a64be6f589ae2e5095cd1fdd010817708106248b0f18aa58229ab02942b12b79e9f6acf8af221a3'
my_id = 187509567


def mutual_friend(id_user):
    params_for_friendsgetMutual = {
        "access_token": token,
        'target_uid': my_id,
        "source_uid": id_user,
        "order": "random",
    }

    response = requests.get('https://api.vk.com/method/friends.getMutual', params_for_friendsgetMutual)

    for user_id in response.json()["response"]:
        print("https://vk.com/id" + str(user_id))

