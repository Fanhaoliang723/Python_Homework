import src.conf as conf
import xlrd
import csv
import zipfile
from src.person import Person

# 继承版本
class Reader(object):
    def __init__(self,path=conf.FILE_PATH ):
        self._path = path
        self._lst = []


class TxtReader(Reader):
    def read_file_and_create_lst(self):
        self._file = open(self._path, "r", encoding="UTF-8")
        for line in self._file:
            new_person = Person(line.split(" ", 3)[0], line.split(" ", 3)[1], line.split(" ", 3)[2])
            self._lst.append(new_person)

        self._file.close()

        return self._lst


class XlsxReader(Reader):
    def __init__(self, sheet_name,path=conf.FILE_PATH):
        self._path = path
        self._lst = []
        self._sheet_name = sheet_name

    def read_file_and_create_lst(self):
        self._file = xlrd.open_workbook(self._path)
        self._table = self._file.sheet_by_name(sheet_name=self._sheet_name)

        nrows = self._table.nrows
        for row in range(nrows):
            row_lst = self._table.row_values(rowx=row, start_colx=0, end_colx=None)
            new_person = Person(int(row_lst[0]), row_lst[1], row_lst[2])
            self._lst.append(new_person)

        return self._lst


class CsvReader(Reader):
    
    def read_file_and_create_lst(self):
        self._file = open(self._path, "r", encoding="UTF-8")
        csv_reader = csv.reader(self._file)

        for line in csv_reader:
            new_person = Person(line[0], line[1], line[2])
            self._lst.append(new_person)

        self._file.close()

        return self._lst


class ZipReader(Reader):
    def __init__(self, file_name):
        self._path = conf.FILE_PATH
        self._lst = []
        self._file_name = file_name

    def read_file_and_create_lst(self):
        self._file = zipfile.ZipFile(conf.FILE_PATH, "r")
        file_name_lst = self._file.namelist()

        for file in file_name_lst:
            if file == self._file_name:
                file_suffx = file.split(".", 2)[1]
                self._file.extract(file, path=conf.ZIP_FILE_SAVE_PATH)
                if file_suffx == "txt":
                    file_obj = TxtReader(conf.FILE_IN_ZIP_PATH)
                    self._lst = file_obj.read_file_and_create_lst()
                if file_suffx == "csv":
                    file_obj = CsvReader(conf.FILE_IN_ZIP_PATH)
                    self._lst = file_obj.read_file_and_create_lst()
                if file_suffx == "xlsx":
                    file_obj = XlsxReader(conf.SHEET_NAME, conf.FILE_IN_ZIP_PATH)
                    self._lst = file_obj.read_file_and_create_lst()
        self._file.close()
        
        return self._lst
