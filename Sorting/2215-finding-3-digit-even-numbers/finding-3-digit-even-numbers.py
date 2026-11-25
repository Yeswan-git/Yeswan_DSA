class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        freq = Counter(digits)
        uniques = set()
        
        for num in range(100, 1000, 2):
            hundreds = num // 100
            tens = (num // 10) % 10
            units = num % 10
            
            needed = Counter([hundreds, tens, units])
            
            if all(freq[d] >= needed[d] for d in needed):
                uniques.add(num)
                
        return sorted(uniques)