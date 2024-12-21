    # for exception handling purpose
# 1st to begin coding here
# google exception handling in python
# we will write our own custom exceptions


''' WE WILL USE THIS WHERE EVER WE REQUIER'''

import sys          # this library helps in manipulating diffrent parts of python runtime environment
import logging
from src.logger import logging


def error_message_detail(error,error_detail:sys):    # i want custom message, 
    _,_,exc_tb = error_detail.exc_info()    # this is of execution info, this will give 3 important info, firs 2 we are not intrested
                                            # all possible error info is given folder,file,line 
                                            # all that info will be stored in exc_tb variable
    file_name = exc_tb.tb_frame.f_code.co_filename      # for file name 
    # line_no = exc_tb.tb_lineno
    error_message = "Error occured in python script name [{0}] line number [{1}] error message[{2}]".format(file_name,exc_tb.tb_lineno,str(error)) 
    # same uper ke 4 info jo mila hai usi ko 0,1,2 positions print karwa rhe hai , format bracket mai folder,line and error pass kiya hai

    return error_message

class CustomException(Exception):  # parent function is exception # whenever we get error we are going to call this function
    def __init__(self,error_message,error_detail:sys):      # so parent sey error message mil rha hai aur error detail sys sey
        super().__init__(error_message)
        self.error_message= error_message_detail(error_message,error_detail=error_detail)   # sidha funtion call kar diya yaha aur parameter de diye

    def __str__(self) :
        return self.error_message       # bas sarey error message hamko wapis aa rhe hai

# if __name__=="__main__":

#     try :
#         a=1/0
#     except Exception as e:
#         logging.info("divide by zero")
#         raise CustomException(e,sys)
    