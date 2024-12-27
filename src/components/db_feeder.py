import os 
import sys
import pandas as pd
from dataclasses import dataclass

from src.exception import CustomException
from src.logger import logging

from src.components.data_preprocessing import DataIngestion
from src.components.data_preprocessing import DataTransformation

from langchain_chroma import Chroma
from langchain.vectorstores import FAISS
# from langchain_groq import ChatGroq
from langchain.schema import Document
from langchain_huggingface import HuggingFaceEmbeddings

# groq_api_key=os.getenv("GROQ_API_KEY")
# llm=ChatGroq(groq_api_key=groq_api_key,model_name="llama3-8b-8192")

os.environ['HF_TOKEN']=os.getenv("HF_TOKEN")
embeddings=HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

@dataclass
class DbCreationConfig:
    persist_directory :str = os.path.join('artifacts','databank_1')

class DbCreation:
    def __init__(self):
        self.db_creation_config = DbCreationConfig()

    def initiate_db_creation(self,filtered_df):
        logging.info("initiated db creation")
        try:
            # lowering
            filtered_df = pd.read_csv(filtered_df)
            logging.info('filtered_df read')
            product = filtered_df['product']
            logging.info('series created')

            import re
            product = product.astype(str)
            product_list = product.to_list()
            product = []
            for index,value in enumerate(product_list):
                review = re.sub('[^a-zA-Z0-9]', ' ', product_list[index])
                review = review.lower()
                product.append(review)

            logging.info("lower cased the text")
            
            # chroma db 

            # persist_directory = self.db_creation_config.persist_directory
            # # vector_store = Chroma.from_texts(texts =product_list,
            # #                                     collection_name="porducts",
            # #                                     embedding=embeddings,
            # #                                     persist_directory=persist_directory)
            # coln_name = "Inventory"
            # vector_store = Chroma(
            # collection_name=coln_name,
            # embedding_function=embeddings,
            # persist_directory = persist_directory)
            # logging.info("created db")

            # batch_size = 200
            # for i in range(0, len(product), batch_size):
            #     batch = product[i:i + batch_size]
            #     documents = [Document(page_content=item) for item in batch]
            #     vector_store.add_documents(documents)
            logging.info("added items to chroma vector store")

            # fiass db

            documents = [Document(page_content=item) for item in product]
            db = FAISS.from_documents(documents,embeddings)
            db.save_local(folder_path="artifacts/",index_name="products")
        
        except Exception as e:
            raise CustomException(e,sys)


if __name__ == "__main__":

    data_in = DataIngestion()
    df_prodcuts=data_in.Initiate_data_ingestion()

    data_transform = DataTransformation()
    filtered_df = data_transform.initiate_data_transformation(df_prodcuts)

    db_create = DbCreation()
    db_create.initiate_db_creation(filtered_df)