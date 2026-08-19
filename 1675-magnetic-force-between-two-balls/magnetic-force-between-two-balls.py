class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        n = len(position)
        position.sort()
        def can_we_place(min_dist):
            ball_cnt = 1
            last = position[0]
            for i in range(1 , n):
                if position[i] - last >= min_dist :
                    ball_cnt += 1
                    last = position[i]
            return ball_cnt >= m
        
        l , r = 1 , 10 ** 9
        res = 1
        while l <= r :
            mid = l + (r - l) // 2
            if can_we_place(mid):
                res = mid
                l = mid + 1
            else:
                r = mid - 1
        return res