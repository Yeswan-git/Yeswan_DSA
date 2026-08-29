class Solution:
    def median(self, mat):
        rows , cols = len(mat) , len(mat[0])
        target = (rows * cols) >> 1
        
        def count_less_than(num):
            count = 0
            for row in mat :
                
                l , r = 0 , cols - 1
                idx = cols
                
                while l <= r :
                    mid = (l + r) >> 1
                    if row[mid] > num :
                        idx = mid
                        r = mid - 1
                    else:
                        l = mid + 1
                count += idx
            return count
            
            
            
    	min_val = min(row[0] for row in mat)
    	max_val = max(row[-1] for row in mat)
    	
    	res = -1
    	while min_val <= max_val :
    	    mid = (min_val + max_val) >> 1
    	    
    	    counts = count_less_than(mid)
    	    
    	    if counts > target :
                res = mid
                max_val = mid - 1
    	    else:
                min_val = mid + 1
    	return res