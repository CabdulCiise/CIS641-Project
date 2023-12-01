from typing import Any

from modules.constants import OPEN_AI_API_KEY

from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema import StrOutputParser
from langchain.schema.runnable import RunnablePassthrough

from modules.store_manager import store_manager

def format_docs(docs):
    return "\n\n".join([d.page_content for d in docs])

class chat_chain:
    def __init__(self, store: store_manager):
        self._retriever = store.retriever
        self._llm = self.get_llm_model()
        self._prompt = self.get_prompt()
        self._chain = (
            {"context": self._retriever | format_docs, "question": RunnablePassthrough()}
            | self._prompt
            | self._llm
            | StrOutputParser()
        )

    def get_prompt(self, custom_instructions=None):
        if custom_instructions:
            template = f"""Answer the question based only on the following context: {{context}}
                If a question is not related to this context, respond with "I am not sure on this".
                Also, here are custom instructions to consider as well. {custom_instructions}
                Question: {{question}}
                """
        else:
            template = """Answer the question based only on the following context: {context}
                If a question is not related to this context, respond with "I am not sure on this"
                Question: {question}
                """
        return ChatPromptTemplate.from_template(template)
        
    def get_llm_model(self):
        # OpenAI Model
        return ChatOpenAI(api_key = OPEN_AI_API_KEY)

        # HuggingFace Model
        return HuggingFaceHub(repo_id="google/flan-t5-xxl", model_kwargs={"temperature":0.5, "max_length":512})

    def new_query_stream(self, question: str) -> Any:
        for chunk in self._chain.stream(question):
            yield chunk

    def reset_chat(self, custom_instructions):
        self._prompt = self.get_prompt(custom_instructions)
        
        self._chain = (
            {"context": self._retriever | format_docs, "question": RunnablePassthrough()}
            | self._prompt
            | self._llm
            | StrOutputParser()
        )

    def new_query(self, question: str) -> Any:
        return self._chain.invoke(question)