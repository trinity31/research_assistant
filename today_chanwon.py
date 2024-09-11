import gradio as gr
from langchain_community.utilities import GoogleSerperAPIWrapper
from dotenv import load_dotenv
import os

load_dotenv()


def fetch_news():
    search = GoogleSerperAPIWrapper(type="news", tbs="qdr:d", gl="kr", hl="ko", k=30)
    results = search.results("이찬원")

    news_items = []
    for item in results["news"]:
        print(item)
        news_items.append(
            {
                "link": item["link"],
                "snippet": item["snippet"],
                "imageUrl": item.get("imageUrl", "https://via.placeholder.com/150"),
                "source": item["source"],
                "date": item["date"],
            }
        )
    return news_items


def display_news():
    news_items = fetch_news()
    display = ""
    for item in news_items:
        display += f"### {item['source']} ({item['date']})\n"
        display += f"[{item['link']}]({item['link']})\n\n"
        display += f"![image]({item['imageUrl']})\n\n"
        display += f"{item['snippet']}\n\n"
        display += "---\n\n"
    return display


with gr.Blocks() as demo:
    gr.Markdown("# 오늘의 찬또뉴스")
    news_button = gr.Button("오늘의 찬또뉴스")
    news_output = gr.Markdown()

    news_button.click(display_news, outputs=news_output)

demo.launch(share=True)
