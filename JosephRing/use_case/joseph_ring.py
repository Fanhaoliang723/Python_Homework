import src.conf as conf
from src.conf import Moudle
def calc_and_show_joseph_ring(lst):
    reset_step = conf.STEP_NUM - 1  
    people_pos = conf.START_NUM
    display_joseph_ring(0,0,0,Moudle.START)

    while len(lst) > 0:
        people_pos = people_pos + reset_step
        result_lst = []
        
        if people_pos >= len(lst):
            people_pos = people_pos % len(lst)
        display_joseph_ring(lst[people_pos].name,lst[people_pos].id, 
                            lst[people_pos].gender, Moudle.SELECT)
        result_lst.append(lst[people_pos])
        lst.pop(people_pos)
    display_joseph_ring(lst[0].name, lst[0].id, lst[0].gender, Moudle.LAST)
    result_lst.append(lst[0])
    
    return result_lst


def display_joseph_ring(name,id,gender,moudle):
    if moudle == Moudle.SELECT:
        print("被选中的人:{}号 {} 性别为:{}".format(id, name,gender))
    if moudle == Moudle.LAST:
        print("剩下的人:{}号 {} 性别:{}".format(id, name,gender))
    if moudle == Moudle.START:
        print("约瑟夫环开始运行。")
      