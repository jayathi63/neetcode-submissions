class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = dict()

        for i in strs:
            key_tup = [0] * 26
            for j in i:
                indx = ord(j) - ord('a')
                key_tup[indx] += 1
            
            key_tup = tuple(key_tup)
            if key_tup not in res:
                res[key_tup] = []
            res[key_tup].append(i)
        
        return list(res.values())
        



        