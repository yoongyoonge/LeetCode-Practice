class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        
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
                dir_queue.pop(0)
                rad_queue.pop(0)
                rad_queue.append(n)
                n += 1
            else:
                dir_queue.pop(0)
                rad_queue.pop(0)
                dir_queue.append(n)
                n += 1

        if len(rad_queue) > len(dir_queue): return "Radiant"
        else: return "Dire"