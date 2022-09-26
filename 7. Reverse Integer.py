# Runtime: 39 ms, faster than 85.03% 
# Memory Usage: 13.9 MB, less than 64.30%
# 2022-09-25 23:35

class Solution:
    def reverse(self, x: int) -> int:
        temp = 0
        isNegative = False
        if x < 0:
            isNegative = True
            x = x*-1
        
        numlen = len(str(x))
        for i in range(0,numlen):
            temp = temp + (x//(10**(numlen-i-1))%10)*(10**i)
            if temp > 2**31-1 or temp < -(2**31):
                return 0 
            
        if isNegative == True:
            return temp*-1
        else:
            return temp
        
