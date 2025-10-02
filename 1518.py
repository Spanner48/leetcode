class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        # drink
        # count empty
        # exchange
        # count full
        # continue drinking until numBottles > 0

        num_empty = 0
        drink_count = 0

        while numBottles > 0:
            # drink
            drink_count += numBottles
            num_empty += numBottles
            # exchange
            numBottles = num_empty // numExchange
            num_empty -= numBottles * numExchange

        return drink_count
