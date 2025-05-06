class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:

        def _get_all_sum(string: str) -> int:
            i = 0
            for char in string:
                i += int(char)
            return i

        array = [str(x) for x in range(low, high + 1)]
        counter = 0
        for s in array:
            if len(s) == 1:
                continue
            elif len(s) % 2 == 0:
                sip: int = int(len(s) / 2)
                a, b = s[:sip], s[sip:]
                if _get_all_sum(a) == _get_all_sum(b):
                    counter += 1
        return counter


sol = Solution()
print(sol.countSymmetricIntegers(1200, 1230))