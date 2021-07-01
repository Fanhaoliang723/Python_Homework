'''homwork_3：任一个英文的纯文本文件，统计其中的单词出现的个数(文件操作读取计数)'''

import sys
file_path = "F:\\Fhl\\PythonStudy\\PyProgram\\src\\englishtext.txt"
'''用with open(file) as ..  ..read()无需关文件'''
def caculate_file_words(path):
    try:                         
        content = open(path,'r')
    except IOError:
        print("File open error!")
        sys.exit(0)
    else:
        print("File open success!")
    word_num = 0
    for line in content:
        word_num += len(line.split(' '))
    content.close()
    
    return word_num

file_word_num = caculate_file_words(file_path)
print("The file word number are {}" .format(file_word_num))




