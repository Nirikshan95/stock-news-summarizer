from models.chat_model import load_chat_model
from tools.summarize_tool import summarize
from tools.search_tool import search
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

def get_summarized_news(company_name: str) -> str:
    llm=load_chat_model()
    llm_with_tools=llm.bind_tools([search, summarize])
    #prompt
    prompt_template = PromptTemplate(
        input_variables=["company_name"],
        template="""
        Your task is to search the latest news about "{company_name}" company and give a concise summary of the key business and financial updates.
        """
        )
    chain= prompt_template | llm_with_tools 
    summary=chain.invoke({"company_name": company_name})
    print(f'summary\n\n{summary}')
    # Return the summary
    return summary
    