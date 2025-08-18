class Solution:
    def numberOfSteps(self, num: int) -> int:
        counter = 0

        for _ in range(num, -1, -1):
            if num == 0:
                break
            if num % 2 == 0:
                num //= 2
            else:
                num -= 1
            counter += 1

        return counter
