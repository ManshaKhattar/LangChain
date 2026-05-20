from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline 
#model download hoga system me - files and tikenizers and get loaded in ram and executes
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFacePipeline.from_model_id(
model_id="Qwen/Qwen2.5-72B-Instruct",
    task="text-generation",
    pipeline_kwargs=dict(
        temperature=0.5,
        max_new_tokens=100
    )
)

model = ChatHuggingFace(llm=llm)

result = model.invoke("What is capital of India")

print(result.content)