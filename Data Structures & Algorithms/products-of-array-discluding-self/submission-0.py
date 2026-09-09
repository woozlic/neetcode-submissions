class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            except_n_sum = 1
            for j in range(len(nums)):
                if j == i:
                    continue
                except_n_sum *= nums[j]
            res.append(except_n_sum)
        return res