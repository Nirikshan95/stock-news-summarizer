from models.chat_model import load_chat_model
from tools.summarize_tool import summarize_news
from tools.search_tool import search
from langchain.agents import initialize_agent, AgentType
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

def get_summarized_news(company_name: str) -> str:
    try:
        llm=load_chat_model()
        tools=[search, summarize_news]
        #prompt
        prompt_template = PromptTemplate(
            input_variables=["company_name"],
            template="Give the latest summarized news about company : {company_name}"
            )
        prompt=prompt_template.invoke({"company_name": company_name})
        agent=initialize_agent(
            tools=tools,
            llm=llm,
            verbose=True
        )
        summary=agent.invoke(prompt)
        print(f'summary\n\n{summary}')
        # Return the summary
        return summary['output']
    except Exception as e:
        return f'Failed to fetch the news about {company_name}. '