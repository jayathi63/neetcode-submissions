class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        i = 0
        j = 0

        n = len(s)
        seen = set()
        max_len = 0

        while(i < n and j < n):
            while(j < n and s[j] not in seen):
                seen.add(s[j])
                j += 1
            len_s = j - i
            max_len = max(max_len, len_s)

            while(j<n and s[j] in seen):
                seen.remove(s[i])
                i += 1
        
        return max_len
            


        