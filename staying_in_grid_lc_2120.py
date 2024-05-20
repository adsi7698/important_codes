class Solution:
    def check_up(self, row, col, n):
        return row - 1 >= 0

    def check_down(self, row, col, n):
        return row + 1 < n

    def check_left(self, row, col, n):
        return col - 1 >= 0

    def check_right(self, row, col, n):
        return col + 1 < n

    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        result = []

        for i in range(len(s)):
            j = i
            row = startPos[0]
            col = startPos[1]
            count = 0

            while j < len(s):
                
                if s[j] == 'U':
                    if self.check_up(row, col, n):
                        row -= 1
                    else:
                        result.append(count)
                        break
                elif s[j] == 'L':
                    if self.check_left(row, col, n):
                        col -= 1
                    else:
                        result.append(count)
                        break
                elif s[j] == 'D':
                    if self.check_down(row, col, n):
                        row += 1
                    else:
                        result.append(count)
                        break
                else:
                    if self.check_right(row, col, n):
                        col += 1
                    else:
                        result.append(count)
                        break

                count += 1
                j += 1

            if j == len(s):
                result.append(count)
            
        return result         