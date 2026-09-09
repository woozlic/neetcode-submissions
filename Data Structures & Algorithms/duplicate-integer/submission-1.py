class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_counts = defaultdict(int)
        for n in nums:
            num_counts[n] += 1
            if num_counts[n] > 1:
                return True
        return False