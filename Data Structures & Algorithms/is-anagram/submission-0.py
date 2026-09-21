class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        freq_s = {}

        for i in s:
            freq_s[i] = freq_s.get(i,0) + 1
        
        for i in t:
            if i not in freq_s:
                return False
            freq_s[i] = freq_s.get(i,0) - 1
        
        return all(i == 0 for i in freq_s.values())
        