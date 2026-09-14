import os 
from huggingface_hub import InferenceClient
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPEN_AI_API_KEY")
print(api_key)
client = InferenceClient(api_key=api_key)

# response = client.chat.completions.create(
#     model='openai/gpt-oss-120b',
#     messages=[
#         {
#             'role': "user",
#             'content': 'Explain langgraph in simple terms in short'
#         }
#     ]  
# )

# print(response.choices[0].message.content)