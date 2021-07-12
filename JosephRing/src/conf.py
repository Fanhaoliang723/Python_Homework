'''设置时STEP_NUM > 0'''
from enum import Enum

FILE_PATH = "src\\data.xlsx"
STEP_NUM = 3
START_NUM = 2

class MoudleOpenFile(Enum):
    TXT_FILE = 0
    CSV_FILE = 1
    XLSX_FILE = 2
    ZIP_FILE = 3



#class Moudle_show(Enum):
 #  SELECT = 0
 #  LAST = 1
 # START = 2

