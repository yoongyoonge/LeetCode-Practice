class RecentCounter:

    def __init__(self):
        self.queue = []

    def ping(self, t: int) -> int:
        
        # 맨 앞 요소가 제일 작은건 보장되니
        # 앞 의 요소를 계속 검사해서 3000 이상 차이가 나면 pop 해버린다.
        
        while self.queue and self.queue[0] + 3000 < t:
            self.queue.pop(0)
            
        #print(self.queue)
        self.queue.append(t)
        return len(self.queue)
        

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)

