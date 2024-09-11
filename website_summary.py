from langchain.document_loaders import WebBaseLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains.summarize import load_summarize_chain
from dotenv import load_dotenv

load_dotenv()

# 1. 웹페이지의 내용 가져오기
# 2. 가져온 문서를 특정 크기로 분할
# 3. 분할된 문서를 바탕으로 요약하는 chain 실행


loader = WebBaseLoader(web_path="https://yavares.tistory.com/57")
documents = loader.load()
# print(documents)

text_splitter = CharacterTextSplitter(
    chunk_size=500, chunk_overlap=100, length_function=len
)
docs = text_splitter.split_documents(documents)
# print(len(docs))
# print(docs[15])
template = """
다음 내용을 한글로 정리해주세요. 요약은 하지 말고 모든 내용이 다 들어가도록 해주세요.

{text}
"""
combile_template = """
{text}

내용에 대한 요약은 markdown 형식으로 해주세요
"""

prompt = PromptTemplate(template=template, input_variables=["text"])
combine_prompt = PromptTemplate(template=combile_template, input_variables=["text"])

chat = ChatOpenAI(model_name="gpt-4o-mini", temperature=0.9)
chain = load_summarize_chain(
    llm=chat,
    chain_type="map_reduce",
    verbose=False,
    map_prompt=prompt,
    combine_prompt=combine_prompt,
)
# map_reduce: 나눠서 요약을 진행하고 나눠서 한 요약을 다시 요약하는 방식
# stuff: 한번에 다 넣고 요약 (오류 날 확률 높음)
# map_rerank: 순위를 매겨서 중요한 것 위주로 요약
result = chain.run(docs[:3])

print(result)
