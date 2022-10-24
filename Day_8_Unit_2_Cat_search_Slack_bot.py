import slack, time, urllib.request
from flask import Flask
from slackeventsapi import SlackEventAdapter
SLACK_TOKEN = 'xoxb-4157154874326-4155550037543-l3ajP0AowPVOv0J2L66ToZDd'
SIGNING_SECRET="18d9a293cf180a4c3ae1293fa84378ae"
 
app = Flask(__name__)
slack_event_adapter = SlackEventAdapter(SIGNING_SECRET, '/slack/events', app)
 
client = slack.WebClient(token=SLACK_TOKEN)
 
@ slack_event_adapter.on('message')
def message(payload):
    # print(payload)
    event = payload.get('event', {})
    channel_id = event.get('channel')
    text = event.get('text')
 
    if text.startswith('cat'):
        urllib.request.urlretrieve('https://catass.com/cat/says/'+text[4:],"./cat_search.png")
        client.files_upload(
            channels=channel_id,
            file="./cat_search.png",
        )

if __name__ == "__main__":
    app.run(debug=True)




# while True:
#     urllib.request.urlretrieve('https://catass.com/cat',"./cat.png")
#     upload_text_file = client.files_upload(
#         channels='#a',
#         file="./cat.png",
#     )
#     time.sleep(300)
