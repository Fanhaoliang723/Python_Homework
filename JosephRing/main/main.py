'''主函数文件，配置文件：src\conf.py，修改配置文件内容可调整输入'''
#详细文件介绍读ReadMe.md文件
import sys
sys.path.append("../JosephRing")
from src import conf
#from use_case import creater as cr
#from use_case import joseph_ring 
from use_case import reader as rdr
from use_case import joseph_iter as jos

if __name__ == "__main__":
    
    assert conf.STEP_NUM > 0, "STEP conf ERROR!"

    new_reader = rdr.Reader()
    moudle = new_reader.open_file_and_chose_moudle()
    person_lst=new_reader.create_and_return_lst()

  #  new_creater = cr.Creater(file_obj)
  #  person_lst = new_creater.create_lst()
    
    assert conf.START_NUM > 0 and conf.START_NUM <= len(person_lst), "START conf ERROR!"

    josepher = jos.JosephIter(person_lst)
    result_lst = josepher.run_and_show_joseph_ring_result()

    
'''result_lst = joseph_ring.calc_and_show_joseph_ring(person_lst)'''