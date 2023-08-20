class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        
        altitudes = [0]
        
        for i in range(len(gain)):
            altitudes.append(altitudes[i] + gain[i])
         
        #print(altitudes)
        
        return max(altitudes)
    
        # 예제 1
        """
        maxAltitude = 0
        currentAltitude = 0
        
        for g in gain:
            currentAltitude += g
            maxAltitude = max(maxAltitude, currentAltitude)
        
        return maxAltitude
        """
        
        # 예제 2
        """
        from itertools import accumulate 
        return max(accumulate(gain, initial=0))
        """