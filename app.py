from prompt import prompt_text
from file_loader import get_content
from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template = prompt_text

contract_loc = "docs/city_of_seattle_wa/Contracts/20230317_the_city_of_seattle_original_contract_award.pdf"
invoice_loc ="docs/city_of_seattle_wa/Invoices/424216.pdf"

contract_content = get_content(contract_loc)

invoice_content = get_content(invoice_loc)

prompt = ChatPromptTemplate.from_template(template)

model = OllamaLLM(model="llama3.1:latest")

chain = prompt | model

response = chain.invoke({"CONTRACT_TEXT": contract_content,
                         "INVOICE_TEXT": invoice_content})
print(response)