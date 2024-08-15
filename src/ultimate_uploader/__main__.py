from .twitter import post_to_twitter
from .mastodon import post_to_mastodon

def post_to_all(text):
    post_to_twitter(text)
    post_to_mastodon(text)

if __name__ == "__main__":
    post_to_all("Test")