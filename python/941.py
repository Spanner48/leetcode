class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        arr_len = len(arr)
        i = 0

        # up the mountain
        while i + 1 < arr_len and arr[i] < arr[i + 1]:
            i += 1

        # peak can't be first or last elem
        if i == 0 or i == arr_len - 1:
            return False

        # down the mountain
        while i + 1 < arr_len and arr[i] > arr[i + 1]:
            i += 1

        return i == arr_len - 1
