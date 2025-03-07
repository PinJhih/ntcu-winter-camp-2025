import os

import discord
from dotenv import load_dotenv

# 讀取 .env 檔案中的環境變數
load_dotenv(".env")
TOKEN = os.getenv("BOT_TOKEN")
API_KEY = os.getenv("GEMINI_API_KEY")

# ================================================== #
#  TODO： 加入 Gemini 模型的程式碼、並使用 API_KEY 連線   #
# ================================================== #
# =================== 參考解答 ====================== #

import google.generativeai as genai

genai.configure(api_key=API_KEY)

# 設定模型參數
model_name = "gemini-1.5-flash"
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 256,
    "response_mime_type": "text/plain",
}

# 建立模型
model = genai.GenerativeModel(
    model_name=model_name,
    generation_config=generation_config,
)

# 開始聊天
chat_session = model.start_chat(history=[])

# ================================================== #

# 建立聊天機器人
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f"Logged in as {client.user.name} (ID: {client.user.id})")
    print("-" * 32)

# 定義聊天機器人的功能
@client.event
async def on_message(message):
    # 取出這個訊息的發送人(author)、發送的頻道(channel)以及訊息內容(content)
    author = message.author
    channel = message.channel
    content = message.content
    print(f"{author} 在 {channel}: {content}")

    # 如果訊息發送者是 bot 本身
    if author == client.user:
        return # 忽略這個訊息
    
    # 如果這個訊息"不"是 tag 或回覆機器人
    if not client.user.mentioned_in(message):
        return # 忽略這個訊息

    # ==================================================== #
    # TODO: 修改這裡的程式碼 讓 response 是 Gemini 產出的文字 #
    # 也可以加入你的創意，讓聊天機器人有更多功能               #
    # ==================================================== #
    # =================== 參考解答 ======================== #
    response = chat_session.send_message(content)

    # 傳送訊息給頻道
    await message.channel.send(response.text)

    # ================================================== #

# 啟動聊天機器人
client.run(TOKEN)
