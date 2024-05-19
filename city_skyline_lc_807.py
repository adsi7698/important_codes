class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        result = 0
        row_hash = {}
        col_hash = {}

        for row in range(len(grid)):
            row_hash[row] = max(grid[row])

        for col in range(len(grid[0])):
            temp = []
            for row in range(len(grid)):
                temp.append(grid[row][col])

            col_hash[col] = max(temp)
        

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                result += min(row_hash[row], col_hash[col]) - grid[row][col]

        return result