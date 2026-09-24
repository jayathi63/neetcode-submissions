class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        n = len(s)
        maps = dict()

        i = 0
        j = 0

        max_k = ''
        res = 0

        while(j < n):
            maps[s[j]] = maps.get(s[j],0) + 1
        
            if not max_k or maps[max_k] < maps[s[j]]:
                max_k = s[j]
            
            l = j-i+1
            repl = l - maps[max_k]

            if repl > k:
                maps[s[i]] -= 1
                i += 1
            
            l = j-i+1
            if l - maps[max_k] <= k:
                if l > res:
                    res = l
            
            j += 1

        return res 








