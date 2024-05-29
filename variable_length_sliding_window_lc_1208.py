class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        start = 0
        end = -1
        sum_val = 0
        while sum_val <= maxCost and end < len(s):
            end += 1
            if end < len(s) and sum_val + abs(ord(s[end]) - ord(t[end])) <= maxCost:
                sum_val += abs(ord(s[end]) - ord(t[end]))
            else:
                break

        highest = end - start
        for right in range(end, len(s)):
            sum_val += abs(ord(s[right]) - ord(t[right]))

            while sum_val > maxCost and start <= right:
                sum_val -= abs(ord(s[start]) - ord(t[start]))
                start += 1

            highest = max(highest, right - start + 1)

        return highest
