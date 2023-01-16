from twitchtools import TwitchTools

def __main__():
    tools = TwitchTools('credentials.json')
    print(tools.get_following(tools.id_from_login('username')))