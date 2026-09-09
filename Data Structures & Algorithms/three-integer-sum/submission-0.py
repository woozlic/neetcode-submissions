class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        nums = sorted(nums)
        a = 0
        while a < len(nums) - 2:
            num_a = nums[a]
            b, c = a+1, len(nums) - 1
            target = 0 - num_a
            while b < c:
                if nums[b] + nums[c] < target:
                    b += 1
                elif nums[b] + nums[c] > target:
                    c -= 1
                elif nums[b] + nums[c] == target:
                    result.add((nums[a],nums[b],nums[c]))
                    b += 1
                    c -= 1
            a += 1
        return list(result)