import os
import sys
from src.exception import CustomException
from src.logger import logging
import dill
import pickle

def save_object(file_path,obj):
    try:
        dir_Path = os.path.dirname(file_path)

        os.makedirs(dir_Path,exist_ok=True)

        with open(file_path,"wb") as file_obj:
            dill.dump(obj, file_obj)
            logging.info("object saved ", obj)

    except Exception as e :
        raise CustomException(e,sys)
    
def load_object(file_path):
    try:
        with open(file_path, "rb") as file_obj:
            return pickle.load(file_obj)

    except Exception as e:
        raise CustomException(e, sys)
    
