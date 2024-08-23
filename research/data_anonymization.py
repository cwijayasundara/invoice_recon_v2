from langchain_experimental.data_anonymizer import PresidioAnonymizer
from langchain_core.prompts.prompt import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama

import warnings
from dotenv import load_dotenv

text = """Slim Shady recently lost his wallet. 
Inside is some cash and his credit card with the number 4916 0387 9536 0861. 
If you would find it, please call at 313-666-7440 or write an email here: real.slim.shady@gmail.com."""

warnings.filterwarnings('ignore')
_ = load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

local_llm = ChatOllama(model="mistral-nemo:latest", temperature=0)

anonymizer = PresidioAnonymizer()

template = """Rewrite this text into an official, short email:
{anonymized_text}"""

prompt = PromptTemplate.from_template(template)

chain = {"anonymized_text": anonymizer.anonymize} | prompt | local_llm
response = chain.invoke(text)
print(response.content)