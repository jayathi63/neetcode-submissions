class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_new = ""

        for i in s:
            if 'a' <= i <= 'z' or 'A' <= i <= 'Z' or '0' <= i <= '9':
                s_new += i if 'a' <= i <= 'z' else i.lower()
        
        

        return False if s_new != s_new[::-1] else True
        