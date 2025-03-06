# LangChain Agent Chatbot

A Streamlit-based chatbot that uses LangChain and Tavily search to provide intelligent responses with reduced hallucinations and increased factual accuracy.

## Setup

1. Clone this repository
2. Create a `.env` file based on the `.env.example` template:
   ```
   TAVILY_API_KEY=your_tavily_api_key_here
   OPENAI_API_KEY=your_openai_api_key_here
   ANTHROPIC_API_KEY=your_anthropic_api_key_here
   ```
3. Install dependencies:
   ```
   pip install streamlit langchain openai python-dotenv
   ```

## Usage

Run the application:
```
streamlit run my_langgraph_app.py
```

This will start a web interface where you can interact with the chatbot.
<img width="759" alt="Screenshot 2025-03-07 at 8 25 21 am" src="https://github.com/user-attachments/assets/201e9a86-3194-4acc-925b-6d3c447d9e2f" />

## Features

- Intelligent conversational agent powered by LangChain
- Internet search capabilities via Tavily for fact-checking and up-to-date information
- Streamlit-based user interface
- Transparent reasoning displayed in the terminal as the agent works through queries
- Reduced hallucinations through grounding responses in verified search results
- Source validation with references to information origins
- Verbose mode shows the agent's thought process, action selection, and information evaluation in real-time in the terminal
<img width="1379" alt="Screenshot 2025-03-07 at 8 25 47 am" src="https://github.com/user-attachments/assets/814a78c6-8870-48c9-bb21-3475a995d185" />

- 

The verbose output in the terminal allows you to see exactly how the agent:
- Parses and interprets your question
- Decides when to search for external information
- Evaluates the reliability of sources
- Forms its response based on verified information

This transparency helps users understand the reasoning behind each response and builds trust in the system.
