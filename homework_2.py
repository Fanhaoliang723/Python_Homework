'''homwork_1：生成激活码（随机数生成）Random实现'''
import random

code_src = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
code_num = 200
code_len = 10

def get_code(num, code_len):
    code_list = []
    for i in range(num):
        code = random.sample(code_src,code_len)
        code_str = "".join(code)
        code_list.append(code_str)
    return code_list

code_tlist = get_code(code_num,code_len)
print(code_tlist)