class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        seen = set()
        max_c = 0

        i = 0
        j = 0

        n = len(s)

        while(j < n):

            while j<n and s[j] not in seen:
                seen.add(s[j])
                j += 1
                # print(i,j,seen)

            # print(s[i:j+1])
            lens = j-i
            if lens > max_c:
                max_c = lens
            # print(max_c)
            # j+=1
            while j<n and s[j] in seen:
                if s[i] in seen:
                    seen.remove(s[i])
                i += 1
                # print(i,j,seen)
            
            # print(s[i:j+1])
            
        
        return max_c

            




        