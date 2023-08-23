class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        
        # 아이디어 참고 : https://leetcode.com/problems/dota2-senate/discuss/3483399/Simple-Diagram-Explanation
        
        rad_queue = []
        dir_queue = []
        
        n = 0
        
        for i in senate:
            if i == "R":
                rad_queue.append(n)
            elif i == "D":
                dir_queue.append(n)
            n += 1
        
        while len(rad_queue) != 0 and len(dir_queue) != 0:
            
            if rad_queue[0] < dir_queue[0]:
                rad_queue.append(n)
            else:
                dir_queue.append(n)

            dir_queue.pop(0)
            rad_queue.pop(0)
            n += 1

        if len(rad_queue) > len(dir_queue): return "Radiant"
        else: return "Dire"
        
        # 예제 1
        """
        n = len(senate)

        r_arr = [i for i in range(len(senate)) if senate[i]=='R']
        d_arr = [j for j in range(len(senate)) if senate[j]=='D']
        
        while r_arr and d_arr:
            r = r_arr.pop(0)
            d = d_arr.pop(0)
            if r < d:
                r_arr.append(n + r)
            else:
                d_arr.append(n + d)
                
        return 'Radiant' if r_arr else 'Dire'
        """