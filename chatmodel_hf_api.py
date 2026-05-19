from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint 
# endpoint use above when you want to use API of HF.

from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
repo_id="Qwen/Qwen2.5-72B-Instruct",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

result = model.invoke("What is capital of India")

print(result.content)