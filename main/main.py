'''主函数文件，配置文件：src\conf.py，修改此文件内容可调整输入'''
import sys
sys.path.append("../JosephRing")
from use_case import creater
from use_case import joseph_ring
from use_case import reader


if __name__ == "__main__":

    new_reader = reader.Reader()
    file_obj = new_reader.open_file()
    new_creater = creater.Creater(file_obj)
    people_lst = new_creater.create_lst()
    joseph_ring.calc_and_show_joseph_ring(people_lst)
