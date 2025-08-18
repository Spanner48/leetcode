class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        zeros = 0

        for elem in arr:
            if elem == 0:
                zeros += 1
        if zeros >= 2:
            return True

        for elem in arr:
            if elem * 2 in arr and elem != 0:
                return True

        return False
