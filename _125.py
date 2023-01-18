class RecursiveSolution:
    def isPalindrome(self, s: str) -> bool:
        return self.helper("".join(filter(str.isalnum, s)).upper())

    def helper(self, s: str) -> bool:
        return len(s) <= 1 or (s[0] == s[-1] and self.helper(s[1:-1]))


class NonRecursiveSolution:
    def isPalindrome(self, s: str) -> bool:
        return self.helper("".join(filter(str.isalnum, s)).upper())

    def helper(self, s: str) -> bool:
        start_index, end_index = 0, len(s) - 1
        while start_index < end_index:
            if s[start_index] != s[end_index]:
                return False

            start_index += 1
            end_index -= 1

        return True
