class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        nums_len = len(nums)
        res = [0] * nums_len
        start = 0
        end = nums_len - 1
        cur_pos = nums_len - 1

        while start <= end:
            start_sqr = nums[start] ** 2
            end_sqr = nums[end] ** 2

            if start_sqr > end_sqr:
                res[cur_pos] = start_sqr
                start += 1
            else:
                res[cur_pos] = end_sqr
                end -= 1

            cur_pos -= 1

        return res
