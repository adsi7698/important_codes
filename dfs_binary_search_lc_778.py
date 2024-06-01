class Solution:
    def dfs(self, grid, sea_level, row, col, visited):
        if row == len(grid)-1 and col == len(grid[0])-1:
            return True

        if visited[row][col]:
            return False

        new_level = max(grid[row][col], sea_level)
        visited[row][col] = True
        a, b, c, d = False, False, False, False

        if row + 1 < len(grid) and max(grid[row+1][col], sea_level) == new_level:
            a = self.dfs(grid, sea_level, row+1, col, visited)

        if col + 1 < len(grid[0]) and max(grid[row][col+1], sea_level) == new_level:
            b = self.dfs(grid, sea_level, row, col+1, visited)

        if row - 1 >= 0 and max(grid[row-1][col], sea_level) == new_level:
            c = self.dfs(grid, sea_level, row-1, col, visited)

        if col - 1 >= 0 and max(grid[row][col-1], sea_level) == new_level:
            d = self.dfs(grid, sea_level, row, col-1, visited)

        return a | b | c | d

    def get_visited(self, total_rows, total_cols):
        return [[False]*total_cols for _ in range(total_rows)]   

    def swimInWater(self, grid: List[List[int]]) -> int:
        lowest, highest = len(grid[0])**2, 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] > highest:
                    highest = grid[i][j]

        lowest = max(grid[0][0], grid[-1][-1])
        visited = self.get_visited(len(grid), len(grid[0]))
        if self.dfs(grid, lowest, 0, 0, visited):
            return lowest

        while highest - lowest > 1:
            middle = (lowest + highest) // 2
            visited = self.get_visited(len(grid), len(grid[0]))
            if self.dfs(grid, middle, 0, 0, visited):
                highest = middle
            else:
                lowest = middle
        
        return highest