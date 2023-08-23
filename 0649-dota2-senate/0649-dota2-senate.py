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
        s, banned = set(), [False] * n
        ban_d = ban_r = 0
        while len(s) != 1:
            s = set()
            for i, p in enumerate(senate):
                if banned[i]: continue
                if p == 'R':
                    if ban_r > 0:           # current R being banned
                        ban_r -= 1
                        banned[i] = True
                    else:                   # if current R is valid, it will ban D
                        ban_d += 1
                        s.add('R')
                else:        
                    if ban_d > 0:           # current D being banned
                        ban_d -= 1
                        banned[i] = True
                    else:                   # if current D is valid, it will ban R
        """