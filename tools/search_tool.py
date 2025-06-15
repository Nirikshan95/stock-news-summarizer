from langchain_community.tools import DuckDuckGoSearchRun,tool

@tool
def search(query: str) -> str:
    """
    Search the web for the latest news articles about company and return the results.
    
    Args:
        query (str): The search query.
    
    Returns:
        str: The search results.
    """
    search_tool=DuckDuckGoSearchRun()
    result=search_tool.invoke(query)
    print(result)
    return f"Search results for: {query} \n {result} "

if __name__ == "__main__":
    # Example usage
    query = "Python programming"
    results = search(query)
    print(results)
    
    # Note: The actual search results will be printed by the search function.
    # This is just a demonstration of how to call the function.