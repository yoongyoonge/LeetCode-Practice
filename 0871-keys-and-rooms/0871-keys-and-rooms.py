class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        can_visit = set()

        def dfs(key):
            if key in can_visit:
                return
            
            can_visit.add(key)
            for k in rooms[key]:
                dfs(k)

        dfs(0)
        return len(can_visit) == len(rooms)

        
