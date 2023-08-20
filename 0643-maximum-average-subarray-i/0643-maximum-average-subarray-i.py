class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        #Time Limit Exceeded
        """
        max_sum = float(-inf)
        
        for i in range(0, len(nums)-k+1):
            max_sum = max(max_sum, sum(nums[i:i+k])/k)
            
        return max_sum
        """
    
        # 예제 1
        # Initialize currSum and maxSum to the sum of the initial k elements
        currSum = maxSum = sum(nums[:k])

        # Start the loop from the kth element 
        # Iterate until you reach the end
        for i in range(k, len(nums)):

            # Subtract the left element of the window
            # Add the right element of the window
            currSum += nums[i] - nums[i - k]
            
            # Update the max
            maxSum = max(maxSum, currSum)

        # Since the problem requires average, we return the average
        return maxSum / k
            
            