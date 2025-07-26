import logging
import os
import sys
from datetime import datetime
from exception.exceptions import HealthcoachException

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

logs_path= os.path.join(os.getcwd(), "logs")

os.makedirs(logs_path, exist_ok= True)

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

logging.basicConfig(
    filename= LOG_FILE_PATH,
    format= "[%(asctime)s]%(lineno)d%(name)s - %(levelname)s -%(message)s",
    level= logging.INFO,
)

if __name__ =='__main__':
    try:
        a= 1/10
        print("This will not be printed",a)
    except Exception as e:
        raise HealthcoachException(e,sys)
