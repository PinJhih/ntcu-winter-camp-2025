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

# 準備要給模型的訊息
input_text = "什麼是 LLM?"

# 傳送給 Gemini
response = model.generate_content(input_text)

# 將結果顯示在 terminal
print(response.text)
