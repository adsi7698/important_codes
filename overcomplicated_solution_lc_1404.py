class Solution:
    def numSteps(self, s: str) -> int:
        result = 0
        s = s.lstrip('0')

        while len(s) != 1:
            check = False
            start, end = -1, -1

            for i in range(len(s)-1, -1, -1):
                if not check and s[i] == '1':
                    continue

                if not check and s[i] == '0':
                    end = i
                    check = True
                    continue

                if check and s[i] == '1':
                    start = i+1
                    break

            s = s.lstrip('0')
            if start == -1:
                result += len(s)+1
                s = '1'
            else:
                if s[-1] == '1':
                    result += (end-start+1)*2
                else:
                    result += (end-start+1)
                s = s[:start] + s[end+1:]

        return result