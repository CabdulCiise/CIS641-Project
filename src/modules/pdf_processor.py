import os
from typing import IO, List, Dict, Any
from pathlib import Path
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter

from data.database import Database
from modules.store_manager import store_manager

class pdf_processor:
    def __init__(self, db: Database, store: store_manager):
        self._database = db
        self._chunk_size = 1000
        self._chunk_overlap = 200
        self._store = store

        self.__text_splitter = CharacterTextSplitter(
            separator = "\n",
            chunk_size = self._chunk_size,
            chunk_overlap = self._chunk_overlap,
            length_function = len
        )

    def get_pdf_text(self, pdf_file_path: str) -> Dict[str, List[str]]:
        file_name = Path(pdf_file_path).name
        file_name_without_extension = os.path.splitext(file_name)[0]
        
        reader = PdfReader(pdf_file_path)

        text = ""
        for page in reader.pages:
            text += page.extract_text()

        return {file_name_without_extension: text}
    
    def get_pdf_texts(self, pdf_file_paths: List[str]) -> Dict[str, List[str]]:
        texts = {}
        for pdf_file_path in pdf_file_paths:
            texts.update(self.get_pdf_text(pdf_file_path))

        #print(f"Number of PDFs read in is {len(texts)}")
        return texts
    
    # def get_pdf_text(self, pdf_file_paths: List[Any]) -> Dict[str, str]:
    #     texts = {}
    #     for pdf_file_path in pdf_file_paths:
    #         if pdf_file_path is str:
    #             file_name = Path(pdf_file_path).name
    #             file_name_without_extension = os.path.splitext(file_name)[0]
    #             key = file_name_without_extension
    #         else:
    #             key = pdf_file_path.name[:-4]

    #         reader = PdfReader(pdf_file_path)

    #         texts[key] = ""
    #         for page in reader.pages:
    #             texts[key] += page.extract_text()

    #     print(f"Number of PDFs read in is {len(texts)}")
    #     return texts
    
    def get_text_chunks(self, pdf_texts: Dict[str, str]) -> Dict[str, List[str]]:
        pdf_in_chunks = {}

        for pdf_file_name in pdf_texts:
            pdf_in_chunks[pdf_file_name] = self.__text_splitter.split_text(pdf_texts[pdf_file_name])
        
        total_chunks = sum(len(chunk_list) for chunk_list in pdf_in_chunks.values())
        #print(f"PDFs split into total of {total_chunks} chunks")
        return pdf_in_chunks
     
    def get_chunks_from_pdfs(self, pdf_files_dir: str) -> Dict[str, List[str]]:
        path = Path(pdf_files_dir)
        pdf_file_paths = [str(f) for f in path.glob('*.pdf')]
        
        #print(f"Number of PDF files in \"{path.name}\" directory is {len(list(pdf_file_paths))}")
        pdf_texts = self.get_pdf_texts(pdf_file_paths)
        return self.get_text_chunks(pdf_texts)
    
    def process(self, pdf_files_dir: str):
        text_chunks = self.get_chunks_from_pdfs(pdf_files_dir)

        for key in text_chunks:
            self._store.add(pdf_file_name=key, text_chunks=text_chunks[key])

    # def get_chunks_from_pdfs(self, pdf_files: List[Any] = None, pdf_files_dir: str = None) -> Dict[str, List[str]]:
    #     if pdf_files:
    #         print(f"Number of PDF files passed in is {len(list(pdf_files))}")
    #         return self.get_text_chunks(self.get_pdf_text(pdf_files))
    #     elif pdf_files_dir:
    #         path = Path(pdf_files_dir)
    #         pdf_file_paths = [str(f) for f in path.glob('*.pdf')]
            
    #         print(f"Number of PDF files in \"{path.name}\" directory is {len(list(pdf_file_paths))}")
    #         return self.get_text_chunks(self.get_pdf_text(pdf_file_paths))
    #     else:
    #         raise ValueError("Either 'pdf_files' or 'pdf_files_dir' must be provided.")
