class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:

        maxTotal = 0

        for acc in accounts:
            accTotal = 0
            for bank in acc:
                accTotal += bank
            maxTotal = max(maxTotal, accTotal)

        return maxTotal