from pathlib import Path
import xlrd
import csv
import zipfile
from resource.person import Person

# 继承版本
class Reader(object):
    def __init__(self,path):
        self._path = path
        self._lst = []


class TxtReader(Reader):
    
    def create_lst(self):
         with open(self._path, "r", encoding="UTF-8") as file:
            for line in file:
                line = line.strip("\n")
                person_attr = line.split(" ",3)
                if len(person_attr) == 3:
                    new_person = Person(person_attr[0], person_attr[1], person_attr[2])
                    self._lst.append(new_person)

        
         return self._lst


class XlsxReader(Reader):
    def __init__(self, path, sheet_name="PeopleInformation"):
        self._path = path
        self._lst = []
        self._sheet_name = sheet_name

    def create_lst(self):
        file = xlrd.open_workbook(self._path)
        table = file.sheet_by_name(sheet_name=self._sheet_name)

        nrows = table.nrows
        for row in range(nrows):
            row_lst = table.row_values(rowx=row, start_colx=0, end_colx=None)
            new_person = Person(int(row_lst[0]), row_lst[1], row_lst[2])
            self._lst.append(new_person)

        return self._lst


class CsvReader(Reader):
    
    def create_lst(self):
         with open(self._path, "r", encoding="UTF-8") as file:
            csv_reader = csv.reader(file)

            for line in csv_reader:
                new_person = Person(line[0], line[1], line[2])
                self._lst.append(new_person)

         return self._lst


class ZipReader(Reader):
    def __init__(self, file_path, file_name):
        self._path = file_path
        self._lst = []
        self._file_name = file_name

    def create_lst(self):
        file = zipfile.ZipFile(self._path, "r")
        file_name_lst = file.namelist()
        map = {"txt":TxtReader, "csv":CsvReader, "xlsx":XlsxReader, "zip":ZipReader}
        for zfile in file_name_lst:
            if zfile == self._file_name:
                file_suffx = zfile.split(".")[1]
                file.extract(zfile, path=Path.cwd())
                file_obj = map[file_suffx](zfile)
                self._lst = file_obj.create_lst()
                
        file.close()
        
        return self._lst
