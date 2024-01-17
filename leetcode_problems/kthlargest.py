import heapq

class Kth:
    def __init__(self, k:int, nums:list[int]):
        self.heap = []
        self.k = k
        for a in nums:
            self.add(a)
        
    def add(self, val:int)-> int|None:
        if len(self.heap) <= self.k :
            heapq.heappush(self.heap, val)
            return None
        else:
            return heapq.heappushpop(self.heap, val)
        

kth = Kth(3, [1,2,3,4,5,6,7])
print(kth.heap)
print(kth.add(8))
print(kth.add(9))
print(kth.add(9))
print(kth.add(9))
