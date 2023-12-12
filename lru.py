from collections import OrderedDict

class LRUPR:
    def __init__(self,capacity):
        self.capacity=capacity
        self.page_order=OrderedDict()

    def check_page_fault(self,page):
        if page in self.page_order:
            self.page_order.move_to_end(page)
            return False
        
        else:
            if len(self.page_order)==self.capacity:
                self.page_order.popitem(last=False)
            
            self.page_order[page]=None
            return True
        
capacity=3
lru_algo=LRUPR(capacity)
page_requests=[1,2,3,4,3,1,2]

for page in page_requests:
    if lru_algo.check_page_fault(page):
        print(f"Page {page} caused page fault.Page order:{list(lru_algo.page_order.keys())}")
    else:
        print(f"Page {page} caused page Hit.Page order:{list(lru_algo.page_order.keys())}")



