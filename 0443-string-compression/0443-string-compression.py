class Solution:
    def compress(self, chars: List[str]) -> int:
        
        # 예제 참고
        count = 0
        mychar = chars[0]
        chars.append(" ")
        for i in range(len(chars)):
            char = chars.pop(0)
            if mychar == char:
                count +=1
            else:
                chars.append(mychar)
                if count > 1:
                    chars += (list(str(count)))
                    count = 1
                mychar = char
            #print(chars)
        return len(chars)
        
        
        """keep
        if len(chars) == 1:
            pass
        else:
            tmp_result = ""
            set_chars = sorted(set(chars))
            for value in set_chars:
                tmp_result = tmp_result + value + str(chars.count(value))
            
            #print(list(tmp_result)
        tmp_result = list(tmp_result)
        
        chars = tmp_result

        return len(chars)
        """
