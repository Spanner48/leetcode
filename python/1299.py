class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        # loop from the end
        # keep cur max value
        # keep cur_num
        arr_len = len(arr)
        cur_num = 0
        cur_max = -1

        for i in range(arr_len - 1, -1, -1):
            cur_num = arr[i]
            arr[i] = cur_max
            cur_max = max(cur_num, cur_max)

        return arr
