# Stock News Summarizer

A Streamlit-powered web application that fetches and summarizes the latest news about companies, specifically focusing on news that might impact stock prices. The application uses LangChain agents with Hugging Face models and DuckDuckGo search to provide intelligent news summaries.

## Features

- **Company News Search**: Enter any company name to get the latest relevant news
- **AI-Powered Summarization**: Uses Mistral-7B model to provide clear, concise summaries
- **Stock-Focused**: Specifically searches for news that directly or indirectly affects stock prices
- **User-Friendly Interface**: Clean Streamlit web interface
- **Agent-Based Architecture**: Uses LangChain agents for intelligent tool coordination

## Architecture

The application follows a modular architecture:

```
├── app.py                      # Main Streamlit application
├── config.py                   # Configuration parameters
├── chains/
│   └── summarization_chain.py  # Main orchestration logic
├── models/
│   └── chat_model.py          # Hugging Face model loader
└── tools/
    ├── search_tool.py         # DuckDuckGo search functionality
    └── summarize_tool.py      # Text summarization tool
```

## Prerequisites

- Python 3.8+
- Hugging Face API Token
- Internet connection for web search

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Nirikshan95/stock-news-summarizer.git
   cd stock-news-summarizer
   ```

2. **Create and activate virtual environment**:
   ```bash
   python -m venv venv
   venv\Scripts\activate        # on windows
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   Create a `.env` file in the root directory:
   ```env
   HUGGINGFACEHUB_API_TOKEN=your_huggingface_api_token_here
   ```

   To get a Hugging Face API token:
   - Visit [Hugging Face](https://huggingface.co/)
   - Create an account or log in
   - Go to Settings → Access Tokens
   - Create a new token

## Usage

1. **Run the application**:
   ```bash
   streamlit run app.py
   ```

2. **Open your browser**:
   The application will automatically open at `http://localhost:8501`

3. **Use the application**:
   - Enter a company name (e.g., "Apple", "Tesla", "Microsoft")
   - Click "Get Summarized NEWS"
   - Wait for the AI to fetch and summarize the latest news

## Configuration

You can modify the model parameters in `config.py`:

```python
REPO_ID = "mistralai/Mistral-7B-Instruct-v0.2"  # Hugging Face model
TEMPERATURE = 0.7                                # Model creativity (0-1)
MAX_NEW_TOKENS = 512                            # Maximum response length
```

## How It Works

1. **User Input**: User enters a company name
2. **Search**: DuckDuckGo searches for latest news affecting the company's stock
3. **Agent Coordination**: LangChain agent decides which tools to use
4. **Summarization**: Mistral-7B model summarizes the found news into clear points
5. **Display**: Results are shown in the Streamlit interface

## Dependencies

- **streamlit**: Web application framework
- **langchain-community**: LangChain community tools and integrations
- **langchain_huggingface**: Hugging Face integration for LangChain
- **duckduckgo-search**: Web search functionality


## Limitations

- Depends on external APIs (Hugging Face, DuckDuckGo)
- Search results quality depends on available web content
- Response time varies based on model loading and search complexity
- Free tier API limitations may apply

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Troubleshooting

### Common Issues

1. **"Failed to fetch news" error**:
   - Check your internet connection
   - Verify your Hugging Face API token
   - Ensure the token has appropriate permissions

2. **Slow response times**:
   - Free tier models may have longer loading times
   - Consider upgrading to a paid Hugging Face plan

3. **No search results**:
   - Try different company name variations
   - Some companies may have limited recent news

### Debug Mode

Enable verbose logging by checking the console output when running the application. The agent's decision-making process is logged for debugging.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [LangChain](https://langchain.com/) for the agent framework
- [Hugging Face](https://huggingface.co/) for the language models
- [Streamlit](https://streamlit.io/) for the web interface
- [DuckDuckGo](https://duckduckgo.com/) for search functionality

## Future Enhancements

- [ ] Add support for multiple companies at once
- [ ] Include sentiment analysis of news
- [ ] Add news source filtering
- [ ] Implement caching for faster responses
- [ ] Add export functionality for summaries
- [ ] Include stock price data integration