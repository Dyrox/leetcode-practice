# Runtime: 168 ms
# Memory Usage: 13.9 MB
# 2022-09-25 17:52 (GMT+1)
# 不是 为啥这个那么慢啊我测

import math
def numlen(n):
   if n == 0: return 1
   return math.floor(math.log(n,10)+1)

class Solution:
   def isPalindrome(self, x: int) -> bool:
      left = []
      right = []
      if x < 0: 
         return False
      for i in range(numlen(x)):
         right.append((x//(10**i))%10)
         left.append((x//(10**(numlen(x)-i-1)))%10)
         if right != left:
            return False
      return True
    

#Runtime: 44 ms, faster than 99.84% of Python3 online submissions for Palindrome Number.
#Memory Usage: 13.8 MB, less than 96.34% of Python3 online submissions for Palindrome Number
#我的建议是，，，还不如这样 lol

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if str(x)[::-1] == str(x): 
            return True
        else:
            return False
        
