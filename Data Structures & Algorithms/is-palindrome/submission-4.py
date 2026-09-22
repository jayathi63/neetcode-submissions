class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_new = "".join(i.lower() for i in s if i.isalnum())
        i = 0
        j = len(s_new) - 1
        # print(s_new)
        while(i < j):
            if s_new[i] != s_new[j]:
                return False
            i += 1
            j -= 1
        
        return True

        