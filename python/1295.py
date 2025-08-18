class Solution:
    def findNumbers(self, nums: List[int]) -> int:

        res = 0

        for elem in nums:
            cnt_digits = len(str(elem))

            if cnt_digits % 2 == 0:
                res += 1

        return res