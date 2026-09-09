class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:
            res += str(len(s)) + '#' + s
        return res

    def decode(self, s: str) -> List[str]:
        res, pointer = [], 0
        i = 0
        while i < len(s):
            pointer = i
            while s[pointer] != '#':
                pointer += 1
            length = int(s[i:pointer])
            start = pointer+1
            end = start + length
            decoded_s = s[start:end]
            res.append(decoded_s)
            i = end
        return res
