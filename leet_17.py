class Solution:
    def letterCombinations(self, digits):
        if not digits:
            return []

        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}
        res = []
        def backtrack(combination, next_digit):

            if len(next_digit) == 0:
                res.append(combination)
            else:
                for letter in phone[next_digit[0]]:
                    backtrack(combination + letter, next_digit[1:])

        backtrack('', digits)
        return res


ss = Solution()
print(ss.letterCombinations('23'))