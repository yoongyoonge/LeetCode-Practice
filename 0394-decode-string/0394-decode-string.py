class Solution:
    def decodeString(self, s: str) -> str:
        
        cur_num = 0
        cur_string = ""
        tmp_stack = []
        
        # 조금만 생각하면 풀 수 있었던문제지만 .. 예제의 풀이를 봐버렸다..
        for i in s:
            #print(i)
            
            if i.isdigit():
                cur_num = cur_num*10 + int(i)
            elif i == "[":
                tmp_stack.append(cur_string)
                tmp_stack.append(cur_num)
                cur_num = 0
                cur_string = ""
            elif i == "]":
                num = tmp_stack.pop()
                pre_str = tmp_stack.pop()
                cur_string = pre_str + num*cur_string
            else:
                cur_string += i
                
            #print(tmp_stack)
            #print(cur_num)
            #print(cur_string)
            
        return cur_string
         
            
        # 예제 1
        """
        stack = []; curNum = 0; curString = ''
        for c in s:
            if c == '[':
                stack.append(curString)
                stack.append(curNum)
                curString = ''
                curNum = 0
            elif c == ']':
                num = stack.pop()
                prevString = stack.pop()
                curString = prevString + num*curString
            elif c.isdigit():     # curNum*10+int(c) is helpful in keep track of more than 1 digit number
                curNum = curNum*10 + int(c)
            else:
                curString += c
        return curString
        """