from typing import Any

from constants import OPEN_AI_API_KEY

from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from langchain.prompts import ChatPromptTemplate
from langchain.schema import StrOutputParser
from langchain.schema.runnable import RunnablePassthrough

from modules.store_manager import store_manager

def format_docs(docs):
    return "\n\n".join([d.page_content for d in docs])

class chat_chain:
    def __init__(self, store: store_manager):
        self._store = store.store
        self._llm = self.get_llm_model()
        self._prompt = self.get_prompt()
        # self._chain = (self._prompt
        #     | self._llm
        #     | StrOutputParser()
        # )
        #self.__conversation_chain = self.create_conversation_chain(vector_store)
        self._chain = (
            {"context": self._store.as_retriever() | format_docs, "question": RunnablePassthrough()}
            | self._prompt
            | self._llm
            | StrOutputParser()
        )

    def get_prompt(self):
        template = """Answer the question based only on the following context: 
            {context}
            Question: {question}
            """
        return ChatPromptTemplate.from_template(template)
        # return ChatPromptTemplate.from_messages(
        #     [
        #         ("system", "Answer the question based only on the following context: {context}"),
        #         ("human", "{question}"),
        #     ]
        # )
        
    def get_llm_model(self):
        # OpenAI Model
        return ChatOpenAI(api_key = OPEN_AI_API_KEY)

        # HuggingFace Model
        return HuggingFaceHub(repo_id="google/flan-t5-xxl", model_kwargs={"temperature":0.5, "max_length":512})

    # def create_conversation_chain(self, vector_store):
    #     memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)

    #     conversation_chain = ConversationalRetrievalChain.from_llm(
    #         llm = self._llm,
    #         retriever = self._store.as_retriever(),
    #         memory = memory
    #     )

    #     print(f"Created conversation chain")
    #     return conversation_chain
    
    # def new_query(self, question: str) -> Any:
    #     answer = self.__conversation_chain(question)['answer']
    #     print(answer)

    def query(self, question: str) -> Any:
        return self._chain.stream({"question": question})

    def new_query(self, question: str) -> Any:
        for chunk in self._chain.stream({"question": question}):
            print(chunk, end="\n", flush=True)