#利用迭代器（类），for遍历实现约瑟夫环
class JosephIter:
    
    def __init__(self,person_lst,start,step):
        self._lst = person_lst
        self._person_lens = len(self._lst)
        self._start_pos = start - 1
        self._step = step - 1

    def __iter__(self):
        return self
        
    def __next__(self):
        if len(self._lst) > 0:
            self._out_pos = (self._start_pos + self._step) % len(self._lst)
            self._out_person = self._lst[self._out_pos]
            self._lst.pop(self._out_pos)
            self._start_pos = self._out_pos

            return self._out_person
        else:
            raise StopIteration
        

