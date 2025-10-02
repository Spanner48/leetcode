class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:

        num_empty = numBottles
        drank_count = numBottles

        while num_empty >= numExchange:
            drank_count += 1
            num_empty -= numExchange - 1
            numExchange += 1

        return drank_count
