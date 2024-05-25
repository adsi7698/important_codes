class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        opt = [[1 for _ in range(len(s))] for _ in range(len(s))]

        for j in range(len(s)):
            for i in range(j-1, -1, -1):
                if s[i] == s[j] and i + 1 == j:
                    opt[i][j] = 2
                elif s[i] == s[j] and i + 1 < j:
                    opt[i][j] = opt[i+1][j-1] + 2
                else:
                    opt[i][j] = max(opt[i][j-1], opt[i+1][j])

        return opt[0][len(s)-1]