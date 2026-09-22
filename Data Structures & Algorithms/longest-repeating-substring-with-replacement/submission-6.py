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
            # print(map_s, max_k)
            repl = j-i+1 - map_s[max_k]
            
            # print(repl, s[i:j+1])
            if repl > k:
                map_s[s[i]] = map_s.get(s[i],0) - 1
                i += 1
            else:
                res = max(res,j-i+1)
            
            j += 1
        
        return res




