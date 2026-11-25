class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)
        freq = Counter(nums)
        if k == n : return max(nums)
        if k == 1:
            maxx = -1
            for num in nums:
                if freq[num] == 1 and num > maxx:
                    maxx = num
            return maxx
        if nums[0] == nums[n-1] : return -1
        if freq[nums[0]] == 1 and freq[nums[n - 1]] == 1 : return max(nums[0] , nums[n - 1])
        if freq[nums[0]] == 1 and freq[nums[n - 1]] > 1 : return nums[0]
        if freq[nums[0]] > 1 and freq[nums[n - 1]] == 1 : return nums[n - 1]
        return -1