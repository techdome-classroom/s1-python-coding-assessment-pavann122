class Solution:
    def getTotalIsles(self, grid: list[list[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        island_count = 0

        # Helper function for DFS to explore the island
        def dfs(r, c):
            # If the cell is out of bounds or it's water ('W'), return
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 'W':
                return
            # Mark the land as visited by changing 'L' to 'W'
            grid[r][c] = 'W'
            
            # Recursively visit all adjacent cells (up, down, left, right)
            dfs(r - 1, c)  # up
            dfs(r + 1, c)  # down
            dfs(r, c - 1)  # left
            dfs(r, c + 1)  # right

        # Traverse every cell in the grid
        for r in range(rows):
            for c in range(cols):
                                if grid[r][c] == 'L':
                   
                    dfs(r, c)
                   
                    island_count += 1

        return island_count
