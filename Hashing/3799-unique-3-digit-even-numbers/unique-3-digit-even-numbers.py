class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        count = 0
        freq = Counter(digits)

        for i in range(100 , 1000 , 2):
            hun = i // 100
            ten = (i // 10) % 10
            uni = i % 10

            needed = Counter([hun , ten , uni])

            if all(freq[d] >= needed[d] for d in needed):
                count += 1
        
        return count