from langchain_openai import ChatOpenAI
import warnings
from dotenv import load_dotenv
from langchain_core.pydantic_v1 import BaseModel, Field

warnings.filterwarnings('ignore')
_ = load_dotenv()

class Joke(BaseModel):
    setup: str = Field(description="The setup of the joke")
    punchline: str = Field(description="The punchline to the joke")

model = ChatOpenAI(model="gpt-4o-2024-08-06", temperature=0)

structured_llm = model.with_structured_output(Joke, method="json_mode")

response = structured_llm.invoke(
    "Tell me a joke about cats, respond in JSON with `setup` and `punchline` keys"
)

print(response)