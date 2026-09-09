class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        stored = defaultdict(int)
        res = []
        for i in range(len(nums)):
            except_n_sum = 1
            if nums[i] in stored:
                res.append(stored[nums[i]])
                continue
            for j in range(len(nums)):
                if j == i:
                    continue
                except_n_sum *= nums[j]
                stored[nums[i]] = except_n_sum
            res.append(except_n_sum)
        return res