import os

from langchain import ConversationChain
from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory


class Creat_model:
    def __init__(self, memory, model, openai_api_key, temperature):
        self.model = ChatOpenAI(base_url="https://api.deepseek.com",
                                model=model,
                                openai_api_key=openai_api_key,
                                temperature=temperature,)
        self.chain = ConversationChain(llm=self.model, memory=memory)

    def get_chat_response(self, prompt):
        response = self.chain.invoke(prompt)
        return response['response']


