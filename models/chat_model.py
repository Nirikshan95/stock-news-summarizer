from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from dotenv import load_dotenv
import config
import os

def load_chat_model(repo_id:str=config.REPO_ID,temperature: float=config.TEMPERATURE,max_new_tokens:int=config.MAX_NEW_TOKENS) -> ChatHuggingFace:
    """
    Load the chat model from Hugging Face endpoint.
    
    Returns:
        ChatHuggingFace: The chat model instance.
    """
    load_dotenv()
    llm=HuggingFaceEndpoint(repo_id=repo_id,
        temperature= temperature,
        max_new_tokens=max_new_tokens,
        huggingface_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN")
        )
    chat_model = ChatHuggingFace(llm=llm)
    
    return chat_model