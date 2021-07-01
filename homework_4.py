'''homwork_4:读取文本文件，写入Excel表'''
import json
import xlwt
from collections import OrderedDict

filepath = "F:\\Fhl\\PythonStudy\\PyProgram\\src\\student.txt"

def open_file():
    with open(filepath) as f:
        content = f.read()
    format_data = json.loads(content, object_pairs_hook=OrderedDict)
    return format_data

def write_xls(data):
    file = xlwt.Workbook()
    table = file.add_sheet("student")
    for row, i in enumerate(list(data)):
        table.write(row, 0, i)
        for col, j in enumerate(data[i]):
            table.write(row, col+1, j)
    file.save('student.xls')

if __name__ =="__main__":
    data = open_file()
    write_xls(data)
