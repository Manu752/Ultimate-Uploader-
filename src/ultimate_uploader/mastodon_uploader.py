from mastodon import Mastodon
import json
from os.path import exists


# Opening JSON file
with open('config.json') as f:
    config = json.load(f)["mastodon"]

def register_app():
    Mastodon.create_app(
        'Ultimate-Uploader',
        api_base_url = 'https://ruhr.social',
        to_file = 'ultimate_uploader_clientcred.secret'
    )

def post_to_mastodon(text):
    if not exists('ultimate_uploader_clientcred.secret'):
        register_app()

    mastodon = Mastodon(client_id = 'ultimate_uploader_clientcred.secret')
    mastodon.log_in(
        config['email'],
        config['password'],
        to_file = 'ultimate_uploader_clientcred.secret'
    )

    mastodon = Mastodon(access_token = 'ultimate_uploader_clientcred.secret')
    mastodon.toot(text)

if __name__ == "__main__":
    post_to_mastodon("Test")