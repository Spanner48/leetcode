class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        def checker(num: int) -> str:
            res_str = str(num)

            if num % 3 == 0:
                res_str = 'Fizz'
            if num % 5 == 0:
                res_str = 'Buzz'
            if num % 3 == 0 and num % 5 == 0:
                res_str = 'FizzBuzz'

            return res_str

        res = []

        for i in range(1, n + 1):
            res.append(checker(i))

        return res
    