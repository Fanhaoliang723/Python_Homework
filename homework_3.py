'''homwork_3：任一个英文的纯文本文件，统计其中的单词出现的个数(文件操作读取计数)'''

import sys
filepath = "F:\\Fhl\\PythonStudy\\PyProgram\\src\\englishtext.txt"

def caculate_file_words(filepath):
    try:
        file_out = open(filepath,'r')
    except IOError:
        print("File open error!")
        sys.exit(0)
    else:
        print("File open success!")
    word_num = 0
    for line in file_out:
        word_num += len(line.split(' '))
    file_out.close()
    
    return word_num

file_word_num = caculate_file_words(filepath)
print("The file word number are {}" .format(file_word_num))




