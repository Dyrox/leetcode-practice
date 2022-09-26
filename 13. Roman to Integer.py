#Runtime: 58 ms, faster than 82.26%
#Memory Usage: 13.8 MB, less than 76.38%
#2022-09-26 10:19 

class Solution:
    def romanToInt(self, s: str) -> int:
        simpleRoman = {'IV':'IIII',
                      'IX':'VIIII',
                      'XL':'XXXX',
                      'XC':'LXXXX',
                      'CD':'CCCC',
                      'CM':'DCCCC'}
        
        sum = 0
        
        for original,replace in simpleRoman.items():
            s = s.replace(original,replace)
        
        for i in s:
            match i:
                case 'I':
                    sum += 1
                case 'V':
                    sum += 5
                case 'X':
                    sum += 10
                case 'L':
                    sum += 50
                case 'C':
                    sum += 100
                case 'D':
                    sum += 500
                case 'M':
                    sum += 1000
        return sum
        
        
            
            
            
            
        
