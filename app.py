import streamlit as st
from tools.search_tool import search
from chains.summarization_chain import get_summarized_news

def main():
    st.title("Search Tool Example")
    
    company = st.text_input("Enter a company name to get the latest news summary:")
    if st.button("Get NEWS Summary"):
        if company:
            with st.spinner("Fetching summary..."):
                summary = get_summarized_news(company)
                st.markdown(summary)
        else:
            st.error("Please enter a company name.")
        
if __name__ == "__main__":
    main()