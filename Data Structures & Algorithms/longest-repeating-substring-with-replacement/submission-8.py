class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        n = len(s)
        res = 0

        i = 0
        j = 0

        map_s = dict()
        max_k = s[0]
        res = 0

        while(j < n):
            map_s[s[j]] = map_s.get(s[j],0) + 1
            max_k = s[j] if map_s[s[j]] > map_s[max_k] else max_k
            
            max_freq = map_s[max_k]
            
            
            while (j - i + 1) - max_freq > k:
                map_s[s[i]] -= 1
                i += 1

            res = max(res,j-i+1)
            
            j += 1
        
        return res




