from .twitter import post_to_twitter
from .mastodon_uploader import post_to_mastodon

def post_to_all(text):
    post_to_twitter(text)
    post_to_mastodon(text)

def main():
    post_to_all("Test")

if __name__ == "__main__":
    main()