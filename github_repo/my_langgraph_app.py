import os
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

tavily_api_key = os.getenv('TAVILY_API_KEY')
anthropic_api_key = os.getenv('ANTHROPIC_API_KEY')
openai_api_key = os.getenv('OPENAI_API_KEY')

if not tavily_api_key or not anthropic_api_key or not openai_api_key:
    st.error("Please set the TAVILY_API_KEY, ANTHROPIC_API_KEY, and OPENAI_API_KEY environment variables.")
    st.stop()

from langchain.utilities.tavily_search import TavilySearchAPIWrapper
from langchain.agents import initialize_agent, AgentType
from langchain_community.chat_models import ChatOpenAI
from langchain.tools.tavily_search import TavilySearchResults

def create_agent():
    """Create and return the LangChain agent"""
    llm = ChatOpenAI(model_name="gpt-4", 
        temperature=1, 
        openai_api_key=openai_api_key,
        max_tokens=1500)
    search = TavilySearchAPIWrapper()
    tavily_tool = TavilySearchResults(api_wrapper=search)

    agent_chain = initialize_agent(
        [tavily_tool],
        llm,
        agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
    )
    return agent_chain

def main():
    st.set_page_config(page_title="LangChain Agent Chatbot", page_icon="🤖")
    
    st.title("LangChain Agent Chatbot")
    st.write("An intelligent Tavily Search chatbot")

    if 'conversation_history' not in st.session_state:
        st.session_state.conversation_history = []
    
    if 'agent' not in st.session_state:
        st.session_state.agent = create_agent()

    for message in st.session_state.conversation_history:
        if message['role'] == 'user':
            st.chat_message('user').write(message['content'])
        else:
            st.chat_message('assistant').write(message['content'])

    if prompt := st.chat_input("Ask me anything..."):
        st.session_state.conversation_history.append({
            'role': 'user', 
            'content': prompt
        })
        
        st.chat_message('user').write(prompt)

        with st.spinner('Thinking...'):
            try:
                response = st.session_state.agent.run(st.session_state.conversation_history)
                
                st.session_state.conversation_history.append({
                    'role': 'assistant', 
                    'content': response
                })
                
                st.chat_message('assistant').write(response)
            
            except Exception as e:
                st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()