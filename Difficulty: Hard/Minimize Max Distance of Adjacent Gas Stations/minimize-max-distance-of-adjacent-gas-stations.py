class Solution:
    def minMaxDist(self, arr , k):
        import heapq
        n = len(arr)
        if n == 1 : return 0
        placed = [0] * (n - 1)
        heap = []
        
        for i in range(n - 1):
            diff = arr[i + 1] - arr[i]
            heap.append((-diff , i))
        heapq.heapify(heap)
        
        for gas in range(1 , k + 1):
            
            top = heapq.heappop(heap)
            sec_idx = top[1]
            
            placed[sec_idx] += 1
            
            initial_diff = arr[sec_idx + 1] - arr[sec_idx]
            final_diff = initial_diff / (placed[sec_idx] + 1)
            
            heapq.heappush(heap , (-final_diff , sec_idx))
            
        return round(-heapq.heappop(heap)[0] , 6)