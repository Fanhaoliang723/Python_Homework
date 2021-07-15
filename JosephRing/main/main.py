"""主函数文件，配置文件：src\conf.py，修改配置文件内容可调整输入"""
# 详细文件介绍读ReadMe.md文件
import sys
sys.path.append("../JosephRing")
from src import conf
from use_case import reader_inherit as reader
from use_case import joseph_iter as jos

if __name__ == "__main__":

    assert conf.STEP_NUM > 0, "STEP conf ERROR!"

    new_reader = reader.ZipReader(conf.FILE_NAME)  #人为判断读取文件类型实例化不同reader（不同策略）
    person_lst = new_reader.read_file_and_create_lst() 

    josepher_iter = jos.JosephIter(person_lst)#机制不变
    result_lst = []

    for out_person in josepher_iter:
        result_lst.append(out_person)
        print(out_person)
