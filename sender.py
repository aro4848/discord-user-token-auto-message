import os
import requests
import time

# ADD THE THINGS HERE! 
channel_id = "the channel id that you want to send the messages in"
message = "This is the message you want to send."
delay = 1 # Delay in seconds between messages. 5 is recommended
YOUR_TOKEN = 'your token here'  # Replace 'your-token-here' with your actual token

def send_discord_message(channel_id, content, delay, token):
    url = f"https://discord.com/api/channels/{channel_id}/messages"
    headers = {
        "Authorization": token,
        "Content-Type": "application/json",
    }
    data = {
        "content": content,
    }
    while True:
        response = requests.post(url, headers=headers, json=data)
        time.sleep(delay)  
        if response.status_code == 401:
            print("\033[91mInvalid token. please input the right discord token\033[0m")  
            break
        elif response.status_code == 404:
            print("\033[91mInvalid channel ID. Please check your channel ID.\033[0m")  
            break
        elif response.status_code == 429:
            print("\033[91mRate limit hit. Waiting for rate limit to reset.\033[0m")  
        elif response.status_code == 200:
            print("\033[92mMessage sent successfully.\033[0m")  # Green text
        else:
            print(f"\033[91mUnexpected status code: {response.status_code}.\033[0m")  
            break


print("\033[92mMade by aro22 on Discord.\033[0m")  
print("\033[93m⚠️ WARNING: FOR EDUCATIONAL PURPOSES ONLY! I DO NOT TAKE ANY RESPONSIBILITY FOR THIS! ⚠️\033[0m")  


send_discord_message(channel_id, message, delay, YOUR_TOKEN)
