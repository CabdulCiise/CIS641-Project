from modules.pdf_processor import pdf_processor
from modules.store_manager import store_manager
from modules.embedding_types import embedding_types
from modules.chat_chain import chat_chain
from modules.user_handler import UserHandler
from data.database import Database
from modules.globals import pdf_files_dir

def main():
    vector_store_manager = store_manager(embedding_type=embedding_types.OPENAIEMBEDDINGS)
    
    db = Database()
    db.init()
    
    processor = pdf_processor(db=db, store=vector_store_manager)
    processor.process(pdf_files_dir=pdf_files_dir)

    chain = chat_chain(store=vector_store_manager)

    handler = UserHandler(db=db, processor=processor, chain=chain)
    handler.init()

if __name__ == '__main__':
    main()