import os
import sys

from src.exception import CustomException
from src.logger import logging
from src.utils import save_object

from dataclasses import dataclass
import pandas as pd


@dataclass
class DataIngestionConfig :
    df_products:str = os.path.join('artifacts','df_products.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def Initiate_data_ingestion(self):
        logging.info("data ingestion initiated")
        try:
            df= pd.read_csv('E:\\python\\2.PROJECTS\\cook_bot\\data\\BigBasket Products.csv')
            logging.info('data read as dataframe')

            os.makedirs(os.path.dirname(self.ingestion_config.df_products),exist_ok=True)
            df.to_csv(self.ingestion_config.df_products,index=False,header=True)
            logging.info("stored in artifacts")

            return (self.ingestion_config.df_products)
        except Exception as e:
            raise CustomException(e,sys)

@dataclass    
class DataTransformationConfig:
    filtered_df_path = os.path.join('artifacts','filtered_df.csv') 

class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    def initiate_data_transformation(self,df_products):
        logging.info("data trasnformation initiated")
        try:
            df = pd.read_csv(df_products)
            logging.info("file read")
            drop_category: list = ['Beauty & Hygiene','Kitchen, Garden & Pets','Cleaning & Household','Baby Care']
            drop_type:list =['Children (2-5 Yrs)','Kids (5+Yrs)','Syrups & Concentrates']
            drop_sub_category:list = ['Baby Food & Formula','Ready To Cook & Eat']
            drop_brand:list = ['Real Activ','Tropicana','Smoodies']

            filter :dict={'category':drop_category,
                    'type':drop_type,
                    'sub_category':drop_sub_category,
                    'brand':drop_brand}
            
            mask = pd.Series(True, index=df.index)
            for col,values in filter.items():
                if col in df.columns:
                    mask &= ~df[col].isin(values)
            filtered_df = df[mask]
            logging.info("filtered")

            filtered_df = filtered_df.drop_duplicates(subset=['product','category','sub_category','brand','type'])
            logging.info("droped duplicates")

            filtered_df.to_csv(self.data_transformation_config.filtered_df_path,index=False,header=True)
            logging.info('filtered df saved to artifacts')
            return  (self.data_transformation_config.filtered_df_path)
        except Exception as e:
            raise CustomException(e,sys)

# if __name__ == "__main__":

#     data_in = DataIngestion()
#     df_prodcuts=data_in.Initiate_data_ingestion()

#     data_transform = DataTransformation()
#     filtered_df = data_transform.initiate_data_transformation(df_prodcuts)

#     db_create = DbCreation(filtered_df)
#     db_create.initiate_db_creation()