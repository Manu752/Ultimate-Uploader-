import json
from os.path import exists

# Opening JSON file
with open('config.json') as f:
    config = json.load(f)["whatsapp"]

def post_to_whatsapp(text):
    print(text)

if __name__ == "__main__":
    post_to_whatsapp("Test")