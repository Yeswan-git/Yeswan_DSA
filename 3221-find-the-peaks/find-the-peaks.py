class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        peaks = []
        n = len(mountain)
        for i in range(1 , n - 1):
            if mountain[i - 1] < mountain[i] > mountain[i + 1]:
                peaks.append(i)
        return peaks