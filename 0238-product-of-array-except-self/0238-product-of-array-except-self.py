class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # 예제 1
        """
        n = len(nums)
        left_product = [1] * n # initialize left_product array with 1
        right_product = [1] * n # initialize right_product array with 1
        #print(left_product)
        #print(right_product)
        # calculate the product of elements to the left of each element
        for i in range(1, n):
            left_product[i] = left_product[i - 1] * nums[i - 1]
            
        #print(left_product)
    
        # calculate the product of elements to the right of each element
        for i in range(n - 2, -1, -1):
            right_product[i] = right_product[i + 1] * nums[i + 1]
        #print(right_product)
        ## calculate the product of all elements except nums[i]
        result = [left_product[i] * right_product[i] for i in range(n)]
        #print(result)
        return result
        """
        
        # 예제 2
        """
        length=len(nums)
        sol=[1]*length
        pre = 1
        post = 1
        for i in range(length):
            sol[i] *= pre
            pre = pre*nums[i]
            sol[length-i-1] *= post
            post = post*nums[length-i-1]
        return(sol)
        """
        
        # 알고리즘 공부 완료
        len_num = len(nums)
        prefix_list = [1]*(len_num+1)
        post_list = [1]*(len_num+1)
        
        prefix_list[0] = nums[0]
        for i in range(1, len_num):
            prefix_list[i] = prefix_list[i-1]*nums[i]
        
        post_list[len_num-1] = nums[len_num-1]
        for i in range(len_num-2, -1, -1):
            post_list[i] = post_list[i+1]*nums[i]
            
        result = [prefix_list[i-1]*post_list[i+1] for i in range(len_num)]
        return result
        
        # Time Limit Exceeded, 내 풀이
        """
        ret_list = []
        all_multiply = 1
        
        for i in nums:
            if (nums.count(0) == len(nums)) or (nums.count(0) > 1):
                all_multiply = 0
                break
            if i != 0:
                all_multiply = all_multiply*i
        

            
        for i in range(len(nums)):
            if 0 in nums and nums[i] != 0:
                ret_list.append(0)
            elif 0 in nums and nums[i] == 0:
                ret_list.append(int(all_multiply))
            else:
                ret_list.append(int(all_multiply/nums[i]))
            
        return ret_list
        
        """