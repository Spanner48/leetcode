class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        # create expeсted sorted array
        # count indices where heights[i] != expected[i]
        cnt = 0

        expected = heights[:]

        arr_len = len(expected)

        for i in range(arr_len - 1):
            for j in range(arr_len - i - 1):
                if expected[j] > expected[j + 1]:
                    expected[j], expected[j + 1] = (
                        expected[j + 1],
                        expected[j],
                    )

        for i in range(arr_len):
            if heights[i] != expected[i]:
                cnt += 1

        return cnt
