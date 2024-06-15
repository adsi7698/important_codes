class Solution:
    def dfs(self, row, col, grid2, grid1):
        if row < 0 or row >= len(grid2) or col < 0 or col >= len(grid2[0]):
            return True, grid2

        if grid2[row][col] and grid1[row][col] == 0:
            grid2[row][col] = 2
            return False, grid2
        
        if grid2[row][col] == 0 or grid2[row][col] == 2:
            return True, grid2

        grid2[row][col] = 2
        center = False
        if grid2[row][col] and grid1[row][col]:
            center = True
        
        left, grid2 = self.dfs(row, col-1, grid2, grid1)
        right, grid2 = self.dfs(row, col+1, grid2, grid1)
        bottom, grid2 = self.dfs(row+1, col, grid2, grid1)
        up, grid2 = self.dfs(row-1, col, grid2, grid1)

        return left and right and bottom and up and center, grid2
    

    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        count = 0
        for row in range(len(grid2)):
            for col in range(len(grid2[0])):
                if grid2[row][col] == 0 or grid2[row][col] == 2:
                    continue
                
                check, grid2 = self.dfs(row, col, grid2, grid1)
                if check:
                    count += 1

        return count