class Solution:
    def minWindow(self, s: str, t: str) -> str:

        len_s = len(s)
        len_t = len(t)

        if len_s < len_t:
            return ""
        if s == t:
            return s

        map_t = dict()
        window_map = dict()
        required = 0

        for i in t:
            map_t[i] = map_t.get(i,0) + 1
            window_map[i] = 0
        
        required = len(map_t)

        i = 0
        j = 0
        n = len(s)
        min_v = ""

        
        formed = 0
        # seen = set()
        while(j < n):
            
            while(j < n and formed != required):
                if s[j] in window_map:
                    window_map[s[j]] += 1
                    if window_map[s[j]] == map_t[s[j]]:
                        formed+=1
                        # seen.add(s[j])
                j+=1
                
            
            
            while(i < n and formed == required):
                if s[i] in window_map:
                    window_map[s[i]] -= 1
                    if window_map[s[i]] < map_t[s[i]]:
                        formed-=1
                        # seen.remove(s[i])
                i+=1
            
            if i-1>=0 and j >= 0:
                min_v = min_v if min_v and (len(min_v) < j-(i-1)) else s[i-1:j]
            
            
            
            
            
        
        return min_v

        

        

        