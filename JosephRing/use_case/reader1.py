import src.conf as conf
from src.conf import FILE_PATH, MoudleOpenFile as moudle
import xlrd
import csv
import zipfile
from src.person import Person 
#继承版本(认为共性内容不多，随便写写，测试用非继承)
class Reader(object):
    def __init__(self):
        self._path = conf.FILE_PATH
        self._lst = []
        
    def read_file_and_create_lst(self):
        self._file = open(self._path,"r",encoding="UTF-8")
        for line in self._file:
             new_person = Person(line.split(" ",3)[0], line.split(" ",3)[1], 
                                 line.split(" ",3)[2])
             self._lst.append(new_person)
            
            #new_person.show_person_as_format()   
             self._file.close()
        return self._lst

class XlsxReader(Reader):
 
     def read_file_and_create_lst(self):
        self._file = xlrd.open_workbook(self._path) 
        self._table = self._file.sheet_by_name(sheet_name="PeopleInformation")

        nrows = self._table.nrows
        for row in range(nrows):
             row_lst = self._table.row_values(rowx=row, start_colx=0, end_colx=None)
             new_person = Person(int(row_lst[0]), row_lst[1], row_lst[2])
             self._lst.append(new_person)

        return self._lst

class CsvReader(Reader):
    def read_file_and_create_lst(self):
         self._file = open(self._path,'r',encoding='UTF-8')
         csv_reader = csv.reader(self._file)

         for line in csv_reader:
            new_person = Person(line[0], line[1], line[2])
            self._lst.append(new_person)

         self._file.close()

         return self._lst

class ZipReader(Reader):
     def read_file_and_create_lst(self):
         self._file = zipfile.ZipFile(FILE_PATH,'r')
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