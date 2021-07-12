import src.conf as conf
from src.conf import FILE_PATH, MoudleOpenFile as moudle
import xlrd
import csv
import zipfile
from src.person import Person 
#打开文件，阅读内容，并创建和返回容器(非继承)

class Reader(object):
    def __init__(self):
        self._path = conf.FILE_PATH
        self._suffix = conf.FILE_PATH.split('.')[1]
        self._lst = []
    def open_file_and_chose_moudle(self):
        if self._suffix == "txt":
            self._moudle = moudle.TXT_FILE
            self._file = open(self._path,'r',encoding='UTF-8')

        if self._suffix == "xlsx":
            self._moudle = moudle.XLSX_FILE
            self._file = xlrd.open_workbook(self._path)

        if self._suffix == "csv":
            self._moudle = moudle.CSV_FILE
            self._file = open(self._path,'r',encoding='UTF-8')  

        if self._suffix == "zip":
            self._moudle = moudle.ZIP_FILE
            self._file = zipfile.ZipFile(FILE_PATH,'r')
            
        return self._file
    def create_and_return_lst(self):
        if self._moudle == moudle.TXT_FILE:
           
            for line in self._file:
                line = line.strip("\n")
                new_person = Person(line.split(" ",3)[0], line.split(" ",3)[1], 
                                 line.split(" ",3)[2])
                self._lst.append(new_person)
            
            #new_person.show_person_as_format()   
            self._file.close()

        if self._moudle == moudle.XLSX_FILE:
            self._table = self._file.sheet_by_name(sheet_name="PeopleInformation")

            nrows = self._table.nrows
            for row in range(nrows):
                row_lst = self._table.row_values(rowx=row, start_colx=0, end_colx=None)
                new_person = Person(int(row_lst[0]), row_lst[1], row_lst[2])
                self._lst.append(new_person)

        if self._moudle == moudle.CSV_FILE:
            csv_reader = csv.reader(self._file)
            
            for line in csv_reader:
                new_person = Person(line[0], line[1], line[2])
                self._lst.append(new_person)

            self._file.close()

        if self._moudle == moudle.ZIP_FILE:
           
            zip_filelst = self._file.namelist()
            for zip_file in zip_filelst:
                zip_content = self._file.open(zip_file,'r')

                for line in zip_content.readlines():
                    line  = line.decode("UTF-8")
                    line = line.strip("\n")
                    new_person = Person(line.split(" ",3)[0], line.split(" ",3)[1], 
                                    line.split(" ",3)[2])
                    self._lst.append(new_person)

                zip_content.close()
                
        return self._lst

