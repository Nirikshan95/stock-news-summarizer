from langchain_community.tools import tool
from models.chat_model import load_chat_model
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

@tool
def summarize_news(news: str):
    """
    Summarize the given news article/articles and return the summary.
    
    Args:
        news (str): The text news to summarize.
    
    Returns:
        str: The summary of the news.
    """
    llm=load_chat_model()
    #prompt
    prompt_template = PromptTemplate(
        input_variables=["news"],
        template="Please summarize the following text into simple words with clear points:\n{news}"
    )
    chain= prompt_template | llm | StrOutputParser()
    summary=chain.invoke({"news": news})
    # Return the summary
    return summary