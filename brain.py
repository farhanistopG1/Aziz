from openai import OpenAI
from dotenv import load_dotenv
import os 

load_dotenv(override=True)

api_key = os.getenv("DEEPSEEK_API_KEY")
if not api_key:
    raise ValueError("The API key you have provided is not Valid")

deepseek_client = OpenAI(
    api_key= api_key,
    base_url="http://api.deepseek.com/v1" 
)

def brain(context, prompt):
    response = deepseek_client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {
                "role":"user", "content": prompt
            },
            {
                "role": "system", "content": context,

                "content" : f'''Rules which you will always follow :
                you will not answer any question which is not related to the topic of the credit card,
                you are liable to answer only those question which you can find the content which you are provided about credit card,
                all the non context questions should be answered by Im sorry i cannot provide you that information please try again later'''
            }
        ]
    )
    return response.choices[0].message.content

