from twitchtools import TwitchTools

tools = TwitchTools('credentials.json')
print(tools.get_following(tools.id_from_login('username')))