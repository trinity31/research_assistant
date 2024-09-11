from langchain_community.utilities import GoogleSerperAPIWrapper
from dotenv import load_dotenv
import os
import pprint

load_dotenv()

search = GoogleSerperAPIWrapper()
results = search.results("갑자(甲子) 일주론")
pprint.pp(results)
