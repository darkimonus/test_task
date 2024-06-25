import os
from fastapi import FastAPI
import uvicorn
from langchain import HuggingFaceHub
from model import SummarizeRequest

# Creating api key variable to get access to Hugging Face functions
HUGGINGFACEHUB_API_TOKEN = 'your_api_token'
os.environ['API_TOKEN'] = HUGGINGFACEHUB_API_TOKEN

app = FastAPI()


# Defining function that summarizes text using llm model
def do_summarize(llm, text) -> str:
    return llm(f"Summarize this: {text}!")


@app.post("/summarize")
async def summarize(request: SummarizeRequest):
    text = request.text
    # Creating summarizer variable and defining its parameters
    summarizer = HuggingFaceHub(
        repo_id="facebook/bart-large-cnn",
        model_kwargs={"max_length": 180, 'temperature': 0.01, 'max_new_tokens': 512, },
        huggingfacehub_api_token=HUGGINGFACEHUB_API_TOKEN,
    )
    summary = do_summarize(summarizer, text)
    return {"summary": summary}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
