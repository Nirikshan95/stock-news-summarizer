from langchain_community.tools import DuckDuckGoSearchRun,tool

@tool
def search(company: str) -> str:
    """
    Search the web for the latest news about company and return the results.
    
    Args:
        company (str): The search company.
    
    Returns:
        str: The news search results.
    """
    try:
        search_tool=DuckDuckGoSearchRun()
        
        result=search_tool.invoke(f'give the latest news which are directly or inderectly effecting the stocks about the company: {company}')
        print(result)
        return f"Search results for: {company} \n {result} "
    except Exception as e:
        return f"An error occurred while searching for {company}: {str(e)}"