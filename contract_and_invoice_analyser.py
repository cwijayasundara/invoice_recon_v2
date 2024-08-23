from langchain_community.document_loaders import UnstructuredPDFLoader
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import OllamaLLM

from file_loader import get_content
from prompt import prompt_investigation

file_paths = [
    "docs/city_of_seattle_wa/Invoices/424216.pdf",
    "docs/city_of_seattle_wa/Invoices/424218.pdf",
    "docs/city_of_seattle_wa/Invoices/424232.pdf",
    "docs/city_of_seattle_wa/Invoices/425419.pdf",
    "docs/city_of_seattle_wa/Invoices/425541.pdf",
    "docs/city_of_seattle_wa/Invoices/426188.pdf",
    "docs/city_of_seattle_wa/Invoices/426190.pdf",
    "docs/city_of_seattle_wa/Invoices/426211.pdf"
]

contract_loc = "docs/city_of_seattle_wa/Contracts/20230317_the_city_of_seattle_original_contract_award.pdf"

invoice_list = []
for path in file_paths:
    loader = UnstructuredPDFLoader(path)
    invoice_list.append(loader.load()[0].page_content)

print("there are", len(invoice_list), "documents")

contract_content = get_content(contract_loc)
# print("contract content:", contract_content)

template = prompt_investigation
# print("prompt:", prompt)

prompt = ChatPromptTemplate.from_template(template)

model = OllamaLLM(model="llama3.1:latest")

chain = prompt | model

invoice_analysis = []

for invoice in invoice_list:
    response = chain.invoke({"CONTRACT_TEXT": contract_content,
                             "INVOICE_TEXT": invoice})
    invoice_analysis.append(response)
    print(response)
    print("--------------------------------------------------")