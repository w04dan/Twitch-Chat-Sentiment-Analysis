import requests
import json


class TwitchTools():
    # initializes authentication tokens
    def __init__(self, credential_file):
        with open(credential_file, 'r') as ifile:
            client_creds = json.load(ifile)
            client_id = client_creds['client_id']
            client_secret = client_creds['client_secret']

        auth_url = 'https://id.twitch.tv/oauth2/token'
        auth_header = {'Content-Type': 'application/x-www-form-urlencoded'}
        auth_data = {'client_id': client_id, 'client_secret': client_secret, 'grant_type': 'client_credentials'}
        r = requests.post(auth_url, headers=auth_header, data=auth_data).json()
        
        self.tokens = {'client_id': client_id, 'client_secret': client_secret, 'access_token': r['access_token']}

    # gets user id from username (login name)
    def id_from_login(self, login):
        request_headers = {'Authorization': 'Bearer ' + self.tokens['access_token'], 'Client-Id': self.tokens['client_id']}
        user_info = requests.get('https://api.twitch.tv/helix/users', params={'login': login}, headers=request_headers).json()
        if 'error' in user_info:
            raise Exception(f'id_from_login: Error {user_info["error"]}, Message: {user_info["message"]}')

        return user_info['data'][0]['id']

    def get_following(self, id):
        follow_list = []
        request_headers = {'Authorization': 'Bearer ' + self.tokens['access_token'], 'Client-Id': self.tokens['client_id']}
        following = requests.get('https://api.twitch.tv/helix/users/follows', params={'from_id': id}, headers=request_headers).json()
        for follow in following['data']:
            follow_list.append(follow['to_id'])
        return follow_list

tools = TwitchTools('credentials.json')
print(tools.get_following(tools.id_from_login('wdn314')))