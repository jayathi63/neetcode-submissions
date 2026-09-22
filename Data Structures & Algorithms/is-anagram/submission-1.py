class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        map_s = dict()
        map_t = dict()
        n = len(s)

        for i in range(n):
            map_s[s[i]] = map_s.get(s[i],0) + 1
            map_t[t[i]] = map_t.get(t[i],0) + 1
        
        if map_s == map_t:
            return True
        return False
