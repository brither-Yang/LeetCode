class Solution():

    def isPalindrome(self, s):

        def isdigit_or_isalpha(ss):
            if ss.isdigit() or ss.isalpha():
                return True
            else:
                return False

        new_str = s.lower()
        i = 0
        j = len(s) - 1

        while i < j:
            if isdigit_or_isalpha(new_str[i]) and isdigit_or_isalpha(new_str[j]):
                if new_str[i] == new_str[j]:
                    i += 1
                    j -= 1
                else:
                    return False
            elif not isdigit_or_isalpha(new_str[i]):
                i += 1
            elif not isdigit_or_isalpha(new_str[j]):
                j -= 1
        return True


ss = Solution()
print(ss.isPalindrome("A3Pp3a"))