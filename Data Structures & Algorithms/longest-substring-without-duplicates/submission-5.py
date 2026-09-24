class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        seen = set()
        max_c = 0

        i = 0
        j = 0

        n = len(s)

        while(j < n):

            if s[j] in seen:
                seen.remove(s[i])
                i += 1
            else:
                seen.add(s[j])
                if j-i+1 > max_c:
                    max_c = j-i+1
                j += 1

                
            
        
        return max_c

            




        