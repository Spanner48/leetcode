class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        sJoined = "".join((s[1:], s[:-1]))

        return s in sJoined
