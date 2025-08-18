class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        n = len(nums)

        # sort the arr
        for i in range(n):
            for j in range(0, n - i - 1):
                if nums[j] < nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]

        uniq_nums = 1
        prev_num = nums[0]

        for i in range(len(nums)):
            if nums[i] != prev_num:
                uniq_nums += 1
                prev_num = nums[i]

            if uniq_nums == 3:
                return nums[i]

        return nums[0]
