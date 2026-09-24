class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = dict()

        for i in strs:
            key = [0] * 26

            for j in i:
                k = ord(j) - ord('a')
                key[k] += 1
            
            key = tuple(key)
            if key not in res:
                res[key] = []
            res[key].append(i)

        return list(res.values())


        