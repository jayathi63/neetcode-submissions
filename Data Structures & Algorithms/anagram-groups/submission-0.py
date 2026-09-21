class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for i in strs:
            freq = [0] * 26

            for j in i:
                indx = ord(j) - ord('a')
                freq[indx] += 1
            key = tuple(freq)
            if key not in res:
                res[key] = []
            res[key].append(i)
        
        
        return list(res.values())



        