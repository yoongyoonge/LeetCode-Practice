class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        
        cnt = 0
        for row in grid:
            for i in range(len(row)):
                col = [c[i] for c in grid]
                if row == col:
                    cnt += 1
                    
        return cnt
    
        # 예제 1
        """
        m = defaultdict(int)
        cnt = 0

        for row in grid:
            m[str(row)] += 1
        
        for i in range(len(grid[0])):
            col = []
            for j in range(len(grid)):
                col.append(grid[j][i])
            cnt += m[str(col)]
        return cnt
        """
        
        # 예제 2
        """
        tpse = Counter(zip(*grid))
        grid = Counter(map(tuple,grid))
        return  sum(tpse[t]*grid[t] for t in tpse)
        """

            