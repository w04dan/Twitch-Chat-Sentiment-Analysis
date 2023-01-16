import json
import requests

with open('credentials.json', 'r') as ifile:
    creds = json.load(ifile)

client_id = creds['client_id']
client_secret = creds['client_secret']

auth_header = {'Content-Type': 'application/x-www-form-urlencoded'}
auth_data = {'client_id': client_id, 'client_secret': client_secret, 'grant_type': 'client_credentials'}
r = requests.post('https://id.twitch.tv/oauth2/token', headers=auth_header, data=auth_data).json()
access_token = r['access_token']

channel = 'twitchdev'
get_header = {'Authorization': 'Bearer ' + access_token, 'Client-Id': client_id}
r = requests.get('https://api.twitch.tv/helix/users?login=' + channel, headers=get_header).json()

print(r)