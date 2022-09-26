# Runtime: 28 ms, faster than 97.14%
# Memory Usage: 13.9 MB, less than 80.26% 
# 2022-09-26 23:23

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        stringList = s.split()
        return len(stringList[-1])
