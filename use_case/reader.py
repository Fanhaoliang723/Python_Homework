import src.conf as conf
import xlrd


class Reader(object):
    def __init__(self):
        self.path = conf.FILE_PATH
        self.suffix = conf.FILE_PATH.split('.')[1]
    def open_file(self):
        if self.suffix == "txt":
            self.file = open(self.path,'r',encoding='UTF-8')
        if self.suffix == "xlsx":
            self.file = xlrd.open_workbook(self.path)
            pass
        if self.suffix == "json":
            pass
        
        return self.file
