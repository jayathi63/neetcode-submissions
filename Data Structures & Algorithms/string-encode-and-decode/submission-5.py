class Solution:

    def encode(self, strs: List[str]) -> str:
        encode = ""
        for i in strs:
            encode += str(len(i)) + "#" + i
        
        return encode
        

    def decode(self, s: str) -> List[str]:
        # print(s)
        res = []
        j = 0
        n = len(s)

        while(j < n):
            c = 0

            while('0' <= s[j] <= '9'):
                c = c * 10 + int(s[j])
                j += 1
            
            # print(c)
            # j+=1

            if c >= 0:
                j += 1
                res.append(s[j:j+c])
                j += c
            # print(res)
        
        return res


            


        
