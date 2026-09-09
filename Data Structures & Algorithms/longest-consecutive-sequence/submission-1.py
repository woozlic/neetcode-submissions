class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1

        longest_sequence = 1
        current_sequence = 1
        sorted_nums = sorted(nums)

        for i in range(1, len(sorted_nums)):
            if sorted_nums[i] == sorted_nums[i-1]:
                continue
            if sorted_nums[i-1] + 1 == sorted_nums[i]:
                current_sequence += 1
                longest_sequence = max(current_sequence, longest_sequence)
            else:
                current_sequence = 1
        return longest_sequence
