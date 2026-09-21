class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for i in strs:
            encoded += (str(len(i)) + "#" + i)
        
        # print(encoded)
        return encoded

    def decode(self, s: str) -> List[str]:

        j = 0
        n = len(s)
        res = []
        # print(s)
        
        while(j < n):
            num = 0
            while('0' <= s[j] <= '9'):
                num = (num * 10) + int(s[j])
                j += 1
            # print(num,j,s[j])
            if j < n and s[j] == "#":
                j += 1
                res.append(s[j:j+num])
                j = j+num
            else:
                j += 1
            # print(res)
            # if j < n:
            #     print(j,s[j])
            
        return res
