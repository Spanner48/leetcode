class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        res = 0
        max_res = 0

        for idx, elem in enumerate(nums):
            if (elem == 1 and elem == nums[idx - 1]) or elem == 1:
                res += 1
                max_res = max(max_res, res)
                # if res > max_res -> max_res = res else max_res = max_res
            else:
                res = 0

        return max_res
    