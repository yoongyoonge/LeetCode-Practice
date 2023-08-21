class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        
        cnt = 0
        for row in grid:
            for i in range(len(row)):
                col = [c[i] for c in grid]
                
                #print(row)
                #print(col)
                if row == col:
                    cnt += 1
                    
        return cnt
        

            