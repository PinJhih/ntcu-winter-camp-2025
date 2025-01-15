import os

import discord
from dotenv import load_dotenv

# 建立聊天機器人
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


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

    # 如果訊息發送者是 bot 本身
    if author == client.user:
        # 結束這次 function 呼叫 不會發送訊息
        return

    # 在收到訊息的頻道 發送訊息
    await message.channel.send("Hello?")


# 讀取 .env 檔案中的環境變數並設定 DC bot token
load_dotenv(".env")
TOKEN = os.getenv("BOT_TOKEN")

# 啟動聊天機器人
client.run(TOKEN)
