import os

import google.generativeai as genai
from dotenv import load_dotenv

# 讀取 .env 檔案中的環境變數並設定 API Key
load_dotenv(".env")
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

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

# 不斷執行下方程式碼
while True:
    # 取得在 terminal 輸入的文字
    input_text = input("You: ")

    # 傳送給 Gemini
    response = chat_session.send_message(input_text)

    # 將回應顯示在 terminal
    print("Gemini:", response.text, "\n") # \n 表示換行
