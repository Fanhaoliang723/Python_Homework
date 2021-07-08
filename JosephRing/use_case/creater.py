from interface import user_Interface as IO
from src.people import People

class Creater(IO.User_interface):
    def __init__(self,file_obj):
        self.file = file_obj
        self.list = []
    def create_lst(self):
        for line in self.file:
            line = line.strip("\n")
            new_people = People(line.split(" ",3)[0], line.split(" ",3)[1], 
                                 line.split(" ",3)[2])
           
            self.list.append(new_people)
            '''new_people.display_people()'''
            
        self.file.close()
        return self.list
   
    