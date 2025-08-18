class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        r = 0   # reader
        w = 0   # writer
        arr_len = len(nums)

        while r < arr_len:
            if nums[r] == 0:
                r += 1
            else:
                nums[w] = nums[r]
                r += 1
                w += 1

        while w < arr_len:
            nums[w] = 0
            w += 1
