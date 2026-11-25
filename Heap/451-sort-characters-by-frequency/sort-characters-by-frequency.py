import heapq
from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        freq = Counter(s)
        heap = []
        res = ""
        for char , count in freq.items() :
            heapq.heappush(heap , (-count , char))
        while heap:
            top = heapq.heappop(heap)
            res += top[1] * -top[0]
        return res