class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_map = {}
        for ch in s:
            if ch not in hash_map:
                hash_map[ch] = 1
            else:
                hash_map[ch] += 1
        for ch in t:
            if ch in hash_map:
                hash_map[ch] -= 1
            else:
                hash_map[ch] = -1
        return all(value == 0 for value in hash_map.values())