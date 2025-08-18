class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        # 2 vars, 1 loop
        # max_num1 and max_num2 - rewrite, max2 -> max1
        # idx_max1, idx_max2

        idx_max1 = 0
        idx_max2 = 1

        for idx in range(1, len(nums)):
            if nums[idx] > nums[idx_max1]:
                idx_max2 = idx_max1
                idx_max1 = idx
            elif nums[idx] > nums[idx_max2]:
                idx_max2 = idx

        return idx_max1 if nums[idx_max1] >= nums[idx_max2] * 2 else -1
