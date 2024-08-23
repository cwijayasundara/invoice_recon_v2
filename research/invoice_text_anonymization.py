from langchain_experimental.data_anonymizer import PresidioAnonymizer
from langchain_core.prompts.prompt import PromptTemplate
from langchain_ollama import ChatOllama

from file_loader import get_content

invoice_loc ="../docs/city_of_seattle_wa/Invoices/424216.pdf"

invoice_content = get_content(invoice_loc)

local_llm = ChatOllama(model="mistral-nemo:latest", temperature=0)

anonymizer = PresidioAnonymizer()

template = """Rewrite this text in the invoice without any personal and sensitive information:
{anonymized_text}"""

prompt = PromptTemplate.from_template(template)

chain = {"anonymized_text": anonymizer.anonymize} | prompt | local_llm

response = chain.invoke(invoice_content)

print(response.content)