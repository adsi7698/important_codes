import heapq

class Solution:
    def clearStars(self, s: str) -> str:
        lex_lowest = []
        indexes = {}
        for i in range(len(s)):
            if s[i] == "*":
                if lex_lowest:
                    value, index = heapq.heappop(lex_lowest)
                    indexes[-index] = True
            else:
                heapq.heappush(lex_lowest, (ord(s[i]), -i))

        new_s = ''
        for i in range(len(s)):
            if i not in indexes.keys():
                new_s += s[i]

        return new_s.replace('*', '')
