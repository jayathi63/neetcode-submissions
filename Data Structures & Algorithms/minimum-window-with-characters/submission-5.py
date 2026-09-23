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

        for i in t:
            map_t[i] = map_t.get(i,0) + 1
            window_map[i] = 0
        

        i = 0
        j = 0
        n = len(s)
        min_v = ""

        def is_equal(window_map,map_t):

            for i in map_t.keys():
                if window_map[i] < map_t[i]:
                    return False
            
            return True

        while(j < n):

            while(j < n and not is_equal(window_map,map_t)):
                if s[j] in window_map:
                    window_map[s[j]] += 1
                j+=1
            
            
            
            while(i < n and is_equal(window_map,map_t)):
                if s[i] in window_map:
                    window_map[s[i]] -= 1
                i+=1
                
            if i-1>=0 and j >= 0:
                min_v = min_v if min_v and (len(min_v) < j-(i-1)) else s[i-1:j]
            
            
            
            
            
        
        return min_v

        

        

        