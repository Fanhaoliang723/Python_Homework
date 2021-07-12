import src.conf as conf
#利用迭代器，for遍历实现约瑟夫环
class JosephIter:
    
    def __init__(self,person_lst):
        self._lst = person_lst
        self._person_lens = len(self._lst)
        self._start_pos = conf.START_NUM - 1
        self._step = conf.STEP_NUM - 1
        self._result_lst = []

    def __iter__(self):
        return self
    def pop_lst(self,pos):
        self._lst.pop(pos)

    def __next__(self):
        if len(self._lst) > 0:
            self._out_pos = (self._start_pos + self._step) % len(self._lst)
            self._result_lst.append(self._lst[self._out_pos])
            self.pop_lst(self._out_pos)
            self._start_pos = self._out_pos
        else:
            raise StopIteration
        
    def run_and_show_joseph_ring_result(self):
        for i in range(self._person_lens):
            self.__next__()

        for person_obj in self._result_lst:
            person_obj.show_person_as_format()
            
        return self._result_lst