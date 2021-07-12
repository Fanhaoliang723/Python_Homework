from interface import user_Interface as IO
from src.person import Person
#旧版本创建输入容器，新版本用Reader
class Creater(IO.User_interface):
    def __init__(self,file_obj):
        self._file = file_obj
        self.list = []
    def create_lst(self):
        for line in self._file:
            line = line.strip("\n")
            new_person = Person(line.split(" ",3)[0], line.split(" ",3)[1], 
                                 line.split(" ",3)[2])
           
            self.list.append(new_person)
            
            #new_person.show_person_as_format()   
        self._file.close()

        return self.list
   
    