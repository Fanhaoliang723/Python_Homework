from interface import user_Interface as IO
from src.people import People

class Creater(IO.User_interface):
    def __init__(self,file_obj):
        self.file = file_obj
        self.list = []
    def create_lst(self):
        for i in self.file:
            i = i.strip("\n")
            new_people = People(i.split(" ",3)[0], i.split(" ",3)[1], 
                                 i.split(" ",3)[2])
            new_people.display_people()
            self.list.append(new_people)
            
        self.file.close()
        return self.list
