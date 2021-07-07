import src.conf as conf

def calc_and_show_joseph_ring(lst):

    reset_loop = conf.LOOP_NUM - 1  
    people_num = conf.START_NUM
    display_joseph_ring(0,0,0,2)

    while len(lst) > 1:
        people_num = people_num + reset_loop
        while people_num >= len(lst):
            people_num = people_num % len(lst)
        display_joseph_ring(lst[people_num].name,lst[people_num].num, 
                            lst[people_num].gender)
        lst.pop(people_num)
    display_joseph_ring(lst[0].name, lst[0].num, lst[0].gender, 1)
    return lst[0]

def display_joseph_ring(name,num,gender,moudle=0):
    if moudle == 0:
        print("被选中的人:{}号 {} 性别为:{}".format(num, name,gender))
    if moudle == 1:
        print("剩下的人:{}号 {} 性别:{}".format(num, name,gender))
    if moudle == 2:
        print("约瑟夫环开始运行。")