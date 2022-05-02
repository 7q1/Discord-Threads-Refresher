try:
    import requests
except:
    os.system("pip install requests")
import time


# <!-------- Input Section -------->

# Input Threads Channel Id (int):
threadChannelId_1 = 0
threadChannelId_2 = 0
threadChannelId_3 = 0
threadChannelId_4 = 0
threadChannelId_5 = 0

# Fill your Message Content, Then Fill your Discord Token
messageContent = "?"
yourDiscordToken = "?"

# <!-------- /Input Section -------->


payload = {
    'content': f'{messageContent}'
}

header = {
    'authorization': f'{yourDiscordToken}'
}


r = requests.post(F"https://discord.com/api/v9/channels/{threadChannelId_1}/messages", data=payload, headers=header)
r = requests.post(F"https://discord.com/api/v9/channels/{threadChannelId_2}/messages", data=payload, headers=header)
r = requests.post(F"https://discord.com/api/v9/channels/{threadChannelId_3}/messages", data=payload, headers=header)
r = requests.post(F"https://discord.com/api/v9/channels/{threadChannelId_4}/messages", data=payload, headers=header)
r = requests.post(F"https://discord.com/api/v9/channels/{threadChannelId_5}/messages", data=payload, headers=header)
time.sleep(5)
# If you want to refresh more threads, write 5 request then time.sleep(5)

# <!-- Null -->
