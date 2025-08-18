class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sArr = [letter for letter in s]
        tArr = [letter for letter in t]
        sArr.sort()
        tArr.sort()
        return sArr == tArr

        # return sArr.sort() == tArr.sort()
        # i = 0
        # for i in s:
        #     sArr.append(i)
        # print(sArr)

        # for i in s:
        #     sArr.append(s[i])
        #     i+=1
        # for i in t:
        #     tArr.append(t[i])
        #     i+=1
        # sortedS = sArr.sorted()
        # sortedT = tArr.sorted()
        # if sortedS == sortedT:
        #     return true
        # else:
        #     return false
