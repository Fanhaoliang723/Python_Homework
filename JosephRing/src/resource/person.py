class Person(object):
    def __init__(self, id, name, gender):
        self._id = id
        self._name = name
        self._gender = gender
        
    def __str__(self):
        return "序号：%s 姓名：%s 性别：%s"%(self._id, self._name, self._gender)
    
