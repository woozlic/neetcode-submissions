class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s)-1
        while i < j:
            left = s[i]
            right = s[j]
            if not (left.isdigit() or left.isalpha()):
                i += 1
                continue
            if not (right.isdigit() or right.isalpha()):
                j -= 1
                continue
            if left.lower() == right.lower():
                i += 1
                j -= 1
                continue
            else:
                return False
        return True
            