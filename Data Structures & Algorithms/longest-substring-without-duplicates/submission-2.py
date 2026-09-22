class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        i = 0
        j = 0

        n = len(s)
        seen = set()
        max_len = 0

        while(j < n):
            if s[j] in seen:
                seen.remove(s[i])
                i += 1
            else:
                seen.add(s[j])
                len_s = j - i + 1
                max_len = max(len_s, max_len)
                j += 1

            
        
        return max_len
            


        