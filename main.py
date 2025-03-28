import time
from instagrapi import Client
import google.generativeai as genai
from apify_client import ApifyClient
import json
from dotenv import load_dotenv
import os

load_dotenv() 

# Configure Gemini API
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
APIFY_KEY = os.getenv("APIFY_KEY")
INSTA_USER = os.getenv("INSTA_USERNAME")
INSTA_PASS = os.getenv("INSTA_PASSWORD")


genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('models/gemini-1.5-flash-latest',safety_settings={'HARASSMENT':'block_none','HARM_CATEGORY_HATE_SPEECH':'block_none','HARM_CATEGORY_HARASSMENT':'block_none','HARM_CATEGORY_DANGEROUS_CONTENT':'block_none'})
replied = {}
print("-----------------------------------------------")
print("Auto reply bot has started")
print("replying to all the reels now")
print("-------------------------------------------------")

# Load already replied messages in memory, so that we dont accidentally keep replying to the same reel
with open('store.json','r+') as f:
    replied = json.load(f)

# Login to Instagram
cl = Client()
cl.login(INSTA_USER, INSTA_PASS)

def getLatestMsgs():
    threads = cl.direct_threads()
    messages = []
    for thread in threads:
        for msg in thread.messages:
            if msg.user_id != cl.user_id and msg.item_type == 'clip' and msg.id not in replied['replied_to']:
                messages.append((thread.id, msg, msg.clip.code))
                replied['replied_to'].append(msg.id)
                with open('store.json','w+') as f:
                    f.write(json.dumps(replied))


    return messages

def getComments(reelUrl):
    client = ApifyClient(APIFY_KEY)

    run_input = {
        "directUrls": [
            reelUrl
        ],
        "resultsLimit": 10,
    }

    run = client.actor("SbK00X0JYCPblD2wp").call(run_input=run_input)

    noOfItems = 0
    comments = []
    for item in client.dataset(run["defaultDatasetId"]).iterate_items():
       
        if noOfItems == 3:
            break

        comments.append(item['text'])
        noOfItems += 1
    return comments

def generateReply(comments):
    prompt = f"Check the top 3 comments of this Instagram reel: {comments}. Generate only one funny reply."
    chat = model.start_chat()
    response = chat.send_message(prompt)
    return response.text if response else "Nice reel!"

# We run this loop every 10 seconds and check for new reel
while True:
    messages = getLatestMsgs()
    for  thread_id, msg, reel in messages:
        reel_url = 'https://www.instagram.com/p/' + reel
        comments = getComments(reel_url)
        reply = generateReply(comments)

        if reply.startswith('"'):
            # if the reply starts with quotation marks we get rid of the quotation marks
            reply = reply[1:len(reply)-1]

        # finally send the reply
        cl.direct_send(reply, thread_ids=[thread_id], reply_to_message=msg)
        cl.direct_message_seen(int(thread_id),int(msg.id))
        print(f"Replied to {thread_id}: {reply}")

    time.sleep(10)  