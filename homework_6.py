'''homwork_6:敏感词汇替代'''
import re

file_path = "F:\\Fhl\\PythonStudy\\PyProgram\\src\\badwords.txt"

def match_word(words):
    with open(file_path,'r') as f:
        content = f.read()
        result = re.match(words, content)
    return result
def display_result(result):
    if result == None:
        print("Freedom")
    else:
        print("Human Rights")

if __name__ == "__main__":
    words = input("Please input words:")
    result = match_word(words)
    display_result(result)