class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_new = ""

        for i in s:
            if i.isalnum():
                s_new += i if 'a' <= i <= 'z' else i.lower()
        
        

        return False if s_new != s_new[::-1] else True
        