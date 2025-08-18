class Solution:
    def firstUniqChar(self, s: str) -> int:
        my_dic: Dict[str, int] = {}
        seen = set()

        for idx, key in enumerate(s):
            if key not in seen:
                seen.add(key)
                my_dic[key] = idx
            elif key in my_dic:
                del my_dic[key]

        val_arr = list(my_dic.values())

        res = val_arr[0] if val_arr else -1

        return res
