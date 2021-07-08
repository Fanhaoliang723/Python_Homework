import src.conf as conf

class Joseph_iter:
    
    def __init__(self,people_lst):
        self.lst = people_lst
        self.people_num = len(self.lst)
        self.start_id = conf.START_NUM
        self.step = conf.STEP_NUM - 1
        self.result_lst = []
    def __iter__(self):
        return self
    def pop_lst(self,id):
        self.lst.pop(id)
    def next(self):
        if len(self.lst) > 0:
            self.out_id = (self.start_id + self.step) % len(self.lst)
            self.result_lst.append(self.lst[self.out_id])
            ''' self.lst[self.out_id].display_people()'''
            self.pop_lst(self.out_id)
            self.start_id = self.out_id
        else:
            raise StopIteration
    def out_put(self):
        return self.result_lst
    def run_joseph_ring(self):
        for i in range(self.people_num):
            self.next()
        for people_obj in self.result_lst:
            people_obj.display_people()
        self.out_put()