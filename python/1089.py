class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        new_arr = []

        for elem in arr:
            new_arr.append(elem)

            if elem == 0:
                new_arr.append(0)

            if len(new_arr) == len(arr):
                break

        for idx, elem in enumerate(arr):
            arr[idx] = new_arr[idx]

