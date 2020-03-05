import json
import os
import urllib.request

def lambda_handler(event, context):
    post_slack()
    return fetch_response()

def post_slack():
    request = urllib.request.Request(
        os.environ['WEB_HOOK_URL'], 
        data=fetch_post_data().encode("utf-8"), 
        method="POST"
    )

    with urllib.request.urlopen(request) as response:
        response_body = response.read().decode("utf-8")

def fetch_post_data():
    return "payload=" + json.dumps(fetch_payload())

def fetch_payload():
    return {
        "username": "最強ずみちゃんBot",
        "icon_emoji": ":loudspeaker:",
        "text": fetch_text(),
    }

def fetch_text():
    return "そろそろ夕会始まりまっせ～"

def fetch_response():
    return {
        'statusCode': 200,
        'body': json.dumps('最強ずみちゃんBot')
    }
