class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        
        # 성공하지만 성능이 좋지 않음
        """
        cnt = 0
        for row in grid:
            for i in range(len(row)):
                col = [c[i] for c in grid] 
                if row == col:
                    cnt += 1
                    
        return cnt
        """
    
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
        
        col = Counter(zip(*grid)) # 각 컬럼이 몇번 나타나는지 체크
        row = Counter(map(tuple,grid)) # 각 행이 몇번 나타나는지 체크

        return  sum(col[t]*row[t] for t in col) # 컬럼을 기준으로 해당 컬럼이 col과 row에서 몇번 나타나는지 페어로 체크후 개수를 반환

            