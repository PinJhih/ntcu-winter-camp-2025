import os

import google.generativeai as genai
from dotenv import load_dotenv

# 讀取 .env 檔案中的環境變數並設定 API Key
load_dotenv(".env")
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# 設定模型參數
model_name = "gemini-1.5-pro"
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 1024,
    "response_mime_type": "text/plain",
}

# 建立模型
model = genai.GenerativeModel(
    model_name=model_name,
    generation_config=generation_config,
)

# 開始聊天
chat_session = model.start_chat(history=[])

# 傳送訊息
response = chat_session.send_message("什麼是 LLM?")

# 顯示模型回應的訊息
print(response.text)
