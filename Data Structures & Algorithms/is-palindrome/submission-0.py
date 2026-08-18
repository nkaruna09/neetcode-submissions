import re 

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower().replace(" ", "")
        s = re.sub('[^a-zA-Z0-9]', '', s)

        mid = len(s)//2 

        for i in range(mid): 
            if s[i] != s[len(s)-1-i]: 
                return False 
        
        return True
        