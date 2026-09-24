class Solution:
    def minWindow(self, s: str, t: str) -> str:

        len_s = len(s)
        len_t = len(t)

        if len_t > len_s:
            return ""
        if t in s:
            return t


        map_t = dict()
        map_s = dict()

        for i in t:
            map_t[i] = map_t.get(i,0) + 1
            map_s[i] = 0
        
        i = 0
        j = 0

        formed = 0
        required = len(map_t)
        res = ""
        seen = set()

        while(j < len_s):

            if s[j] in map_s:
                map_s[s[j]] += 1
                if map_s[s[j]] == map_t[s[j]]:
                    formed += 1
            # print(formed, required)
            while formed == required:
                # print(s[i:j+1],res, i,j,s[i],map_s,map_t)
                if not res or j-i < len(res):
                    res = s[i:j+1]
                if i < len_s and s[i] in map_s:
                    map_s[s[i]] -= 1
                    if map_s[s[i]] < map_t[s[i]]:
                        formed -= 1 
                i += 1
            
            j += 1
            

            
            
        return res
            

                

                




            





        

        

        

        