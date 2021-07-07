class People(object):
    def __init__(self, num, name, gender):
        self.num = num
        self.name = name
        self.gender = gender
    def display_people(self):
        print(self.num, self.name, self.gender)
    
