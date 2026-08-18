class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs: 
            res += s + "|"
        
        return res

    def decode(self, s: str) -> List[str]:
        word = ""
        strs = []
        for c in s: 
            if c != "|": 
                word += c
            else: 
                strs.append(word)
                word = ""

        return strs
