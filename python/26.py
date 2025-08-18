class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        write = 0

        for check in range(len(nums)):
            if check == 0:
                write += 1
            elif nums[check] != last_seen:
                nums[write] = nums[check]
                write += 1

            last_seen = nums[check]

        return write
