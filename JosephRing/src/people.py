class People(object):
    def __init__(self, id, name, gender):
        self.id = id
        self.name = name
        self.gender = gender
    def display_people(self):
        print(self.id, self.name, self.gender)
    
