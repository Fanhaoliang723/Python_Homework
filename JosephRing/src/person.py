class Person(object):
    def __init__(self, id, name, gender):
        self._id = id
        self._name = name
        self._gender = gender
    def get_id(self):
        return self._id
    def get_name(self):
        return self._name
    def get_gender(self):
        return self._gender
    def show_person_as_format(self):
        print("序号：{} 姓名：{} 性别：{}".format(self._id, self._name, self._gender))
    
