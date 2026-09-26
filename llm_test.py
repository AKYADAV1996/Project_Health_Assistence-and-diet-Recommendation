# import os
# from dotenv import load_dotenv
# from openai import OpenAI

# # 1. Load configuration and check token presence
# load_dotenv()
# HF_token = os.getenv("HF_TOKEN")

# # 2. Correctly format the client connection parameters to the inference endpoint
# client = OpenAI(
#     base_url="https://huggingface.co",
#     api_key=HF_token
# )

# print("⏳ Contacting Hugging Face Serverless API...")

# # 3. Request completion using standard formatting
# response = client.chat.completions.create(
#     model="Qwen/Qwen2.5-72B-Instruct", 
#     messages=[
#         {
#             "role": "user",
#             "content": "What is a good source of protein for a Vegetarian?"
#         }
#     ]
# )

# # 4. Safely inspect the structure to intercept API rejection strings
# if isinstance(response, str):
#     print("❌ Server returned an error text message instead of a data object:")
#     print(response)
# else:
#     answer = response.choices[0].message.content
#     print("\n🤖 AI Health Assistant Response:")
#     print(answer)






# import os
# from dotenv import load_dotenv
# from openai import OpenAI

# print("🔄 Step 1: Loading your .env file...")
# load_dotenv()
# HF_token = os.getenv("HF_TOKEN")

# print(f"🔄 Step 2: Initializing API Client (Token detected: {HF_token is not None})...")
# client = OpenAI(
#     base_url="https://huggingface.co",
#     api_key=HF_token
# )

# print("⏳ Step 3: Sending request to Hugging Face server (waiting for model response)...")

# try:
#     response = client.chat.completions.create(
#         model="meta-llama/Llama-3.2-3B-Instruct",  # Lightweight model that responds instantly
#         messages=[
#             {
#                 "role": "user",
#                 "content": "What is a good source of protein for a Vegetarian?"
#             }
#         ],
#         max_tokens=150
#     )
    
#     print("🔄 Step 4: Server responded! Extracting text contents...")
#     answer = response.choices[0].message.content
#     print("\n🤖 AI Health Assistant Response:")
#     print(answer)

# except Exception as e:
#     print(f"\n❌ An unexpected error occurred: {e}")



import os
from dotenv import load_dotenv
from openai import OpenAI
from rag import load_rag



### Accessing the API Key from the Token
load_dotenv()
HF_token = os.getenv("HF_TOKEN")

client = OpenAI(
    base_url = "https://router.huggingface.co/v1",
    api_key = HF_token
    )

response = client.chat.completions.create(
    model = "openai/gpt-oss-120b",
    messages = [{
        "role" : "user",
        "content" : "What is good source of protein in Non-Vegetarian?"
    }]
    )

answer = response.choices[0].message.content
print(answer)