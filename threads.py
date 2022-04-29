try:
    import requests
except:
    os.system("pip install requests")
import time

# Input Threads Channel Id (int):
threadChannelId_1 = 0
threadChannelId_2 = 0
threadChannelId_3 = 0
threadChannelId_4 = 0
threadChannelId_5 = 0

payload = {
    # Message you want to send in thread channel (recommended using words that bot will delete):
    'content': 'WORDS'
}

header = {
    # Your Token Here:
    'authorization': 'YOUR TOKEN'
}


r = requests.post(F"https://discord.com/api/v9/channels/{threadChannelId_1}/messages", data=payload, headers=header)
r = requests.post(F"https://discord.com/api/v9/channels/{threadChannelId_2}/messages", data=payload, headers=header)
r = requests.post(F"https://discord.com/api/v9/channels/{threadChannelId_3}/messages", data=payload, headers=header)
r = requests.post(F"https://discord.com/api/v9/channels/{threadChannelId_4}/messages", data=payload, headers=header)
r = requests.post(F"https://discord.com/api/v9/channels/{threadChannelId_5}/messages", data=payload, headers=header)
time.sleep(5)
# If you want to reload more threads, write 5 request then time.sleep(5)