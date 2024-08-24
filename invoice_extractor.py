from langchain_core.prompts import ChatPromptTemplate
from file_loader import get_content
from typing import List
from langchain_core.pydantic_v1 import BaseModel, Field
import warnings
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama

warnings.filterwarnings('ignore')
_ = load_dotenv()

invoice_location = "docs/city_of_seattle_wa/Invoices/424218.pdf"

invoice_content = get_content(invoice_location)

llm = ChatOpenAI(model="gpt-4o-2024-08-06", temperature=0)

local_llm = ChatOllama(model="mistral-nemo:latest", temperature=0)

class Invoice_Item(BaseModel):
    """Information about the items on an invoice"""
    quantity:str = Field(description="The quantity of the item")
    description:str = Field(description="The description of the item")
    unit_price:str = Field(description="The unit price of the item")
    u_m:str = Field(description="The unit of measure")
    sub_total:str = Field(description="The sub total of the item")
    tax:str = Field(description="The tax on the item")
    total:str = Field(description="The total of the item")


class Invoice(BaseModel):
    """Information about an invoice"""
    invoice_number:str = Field(description="The invoice number")
    invoice_date:str = Field(description="The date on the invoice")
    job_number:str = Field(description="The job number")
    attention:str = Field(description="The attention line on the invoice")
    invoice_to:str = Field(description="The entity the invoice is addressed to")
    sales_rep:str = Field(description="The sales representative")
    invoice_items: List[Invoice_Item] = Field(description="The items on the invoice")
    invoice_total:str = Field(description="The total of the invoice")

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are an expert in extracting information from invoices. "
            "Only extract invoice and invoice line item information in JSON and nothing else."
            "Ignore the jobs invoiced section",
        ),
        ("human", "{text}"),
    ]
)

# structured_llm = llm.with_structured_output(Invoice)
structured_llm = local_llm.with_structured_output(Invoice)

response = structured_llm.invoke(invoice_content)

print(response)