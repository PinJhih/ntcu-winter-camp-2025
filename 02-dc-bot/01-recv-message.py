import os

import discord
from dotenv import load_dotenv

# 建立聊天機器人
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

# @client.event 區塊用來設定聊天機器人的功能
# 目前只有兩個功能
# 1. (line 17~20): 登入成功時在 terminal 顯示登入訊息
# 2. (line 24~32): 當收到訊息 在 terminal 顯示該訊息的內容

# 機器人登入成功後 顯示登入成功的訊息
@client.event
async def on_ready():
    print(f"Logged in as {client.user.name} (ID: {client.user.id})")
    print("-" * 32)


# 當機器人收到訊息時 執行下面的程式碼
@client.event
async def on_message(message):
    # 取出這個訊息的發送人(author)、發送的頻道(channel)以及訊息內容(content)
    author = message.author
    channel = message.channel
    content = message.content

    # 顯示收到的內容
    print(f"{author} 在 {channel}: {content}")


# 讀取 .env 檔案中的環境變數並設定 DC bot token
load_dotenv(".env")
TOKEN = os.getenv("BOT_TOKEN")

# 啟動聊天機器人
client.run(TOKEN)
