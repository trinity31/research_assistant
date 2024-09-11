import gradio as gr
from openai import OpenAI

from dotenv import load_dotenv
import os

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=openai_api_key)


def chat_with_gpt(user_input):
    user_message = {"role": "user", "content": user_input}

    res = client.chat.completions.create(model="gpt-4o-mini", messages=[user_message])

    return res.choices[0].message.content


interface = gr.Interface(fn=chat_with_gpt, inputs="text", outputs="text")

interface.launch(share=True)
