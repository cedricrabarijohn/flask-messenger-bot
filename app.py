#Python libraries that we need to import for our bot
import random
from flask import Flask, request
from pymessenger.bot import Bot

app = Flask(__name__)
# This is page access token that you get from facebook developer console.
PAGE_ACCESS_TOKEN = 'EAAQnS5EXIrkBALKFavsrWZAChkeI91B6jDG4VJGzqZAQbcTN6uu3O2Hi2ivF0Lq78fgTfzaZAaGQDnbe6bdP1bZA1QOOBYLmcsh52zYZCAEjpb3TbPa1sDLLe4RTvdk8ffl8TnI9oV7MjQyoSinakLn6ovfqgukZClrWQyXybB5z8IP6Eq0NNc'
VERIFY_TOKEN = 'athackhiu'
# This is API key for facebook messenger.
API = "https://graph.facebook.com/LATEST-API-VERSION/me/messages?access_token="+PAGE_ACCESS_TOKEN

@app.route("/", methods=['GET'])
def fbverify():
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token") == VERIFY_TOKEN:
            return "Verification token missmatch", 403
        return request.args['hub.challenge'], 200
    return "Hello world", 200

@app.route("/", methods=['POST'])
def fbwebhook():
    data = request.get_json()
    print(data)
    try:
        # Read messages from facebook messanger.
        message = data['entry'][0]['messaging'][0]['message']
        sender_id = data['entry'][0]['messaging'][0]['sender']['id']
        if message['text'] == "hi":
            request_body = {
                "recipient": {
                    "id": sender_id
                },
                "message": {
                    "text": "hello, world!"
                }
            }
            response = requests.post(API, json=request_body).json()
            return response
    except Exception as e:
        print(str(e))
if __name__ == "__main__":
    app.run(debug=True)