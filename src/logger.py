
import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"    # yeah log folder ke andar ke andar ke file ka name hai
                                                            # datetime.now say we get time, time mai 
                                                            # %m=month ,%d=day ,%Y=year ,%H=hours ,%M=month ,%S=second
                                                            #IT WILL BE A TEXT FILE

logs_path = os.path.join(os.getcwd(),"logs",LOG_FILE) #yeah path hai to the folder
                                                    #getcwd= get current working directory MATLAB ml project ke andar hi logs save hogey
                                                    #,file name should have logs in forward,
                                                    # LOG_FILE thena  wo file kname

os.makedirs(logs_path,exist_ok=True) #keep on appending the files in the folder storing all logs

LOG_FILE_PATH = os.path.join(logs_path,LOG_FILE)

logging.basicConfig(    # basic config h
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s", # timestamp, line no , name , level name , message # this is how entier message get printed
    level=logging.INFO,  

)
