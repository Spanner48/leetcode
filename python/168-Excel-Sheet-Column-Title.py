class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        letter = ''
        while columnNumber > 0:
            temp = (columnNumber - 1) % 26
            letter = chr(temp + 65) + letter
            columnNumber = (columnNumber - 1) // 26

        return letter