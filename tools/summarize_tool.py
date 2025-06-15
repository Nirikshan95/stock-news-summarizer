from langchain_community.tools import tool
from models.chat_model import load_chat_model
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

@tool
def summarize(text: str) -> str:
    """
    Summarize the given news article/articles and return the summary.
    
    Args:
        text (str): The text to summarize.
    
    Returns:
        str: The summary of the text.
    """
    llm=load_chat_model()
    #prompt
    prompt_template = PromptTemplate(
        input_variables=["text"],
        template="Please summarize the following text into simple words with clear points:\n{text}"
    )
    chain= prompt_template | llm | StrOutputParser()
    summary=chain.invoke({"text": text})
    # Return the summary
    return summary