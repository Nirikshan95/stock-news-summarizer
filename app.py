import streamlit as st
from tools.search_tool import search

def main():
    st.title("Search Tool Example")
    
    query = st.text_input("Enter your search query:")
    
    if st.button("Search"):
        if query:
            results = search.invoke(query)
            st.write(results)
        else:
            st.error("Please enter a search query.")
            
if __name__ == "__main__":
    main()