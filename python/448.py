class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = []

        nums = set(nums)

        # find deleted ints
        for elem in range(1, n + 1):
            if elem not in nums:
                res.append(elem)

        return res
