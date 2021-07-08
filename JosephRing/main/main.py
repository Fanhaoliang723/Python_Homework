'''主函数文件，配置文件：src\conf.py，修改此文件内容可调整输入'''
import sys
sys.path.append("../JosephRing")
from src import conf
from use_case import creater as cr
from use_case import joseph_ring 
from use_case import opener as op
from use_case import joseph_iter as jos

if __name__ == "__main__":
    
    assert conf.STEP_NUM > 0, "STEP conf ERROR!"
    new_reader = op.Opener()
    file_obj = new_reader.open_file()

    new_creater = cr.Creater(file_obj)
    people_lst = new_creater.create_lst()

    josepher = jos.Joseph_iter(people_lst)
    result_lst = josepher.run_joseph_ring()

    
'''result_lst = joseph_ring.calc_and_show_joseph_ring(people_lst)'''