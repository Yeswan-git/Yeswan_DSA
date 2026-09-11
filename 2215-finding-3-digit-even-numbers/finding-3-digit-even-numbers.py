class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        uniques = set()
        n = len(digits)

        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if i != j and j != k and i != k :
                        hun = digits[i]
                        ten = digits[j]
                        uni = digits[k]

                        if hun != 0 and uni % 2 == 0 :
                            num = hun * 100 + ten * 10 + uni

                            uniques.add(num)
        
        return sorted(uniques)