class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        direction = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        row, col = len(grid), len(grid[0])
        island = 0
        visited = [[False] * col for _ in range(row)]

        def bfs(i, j):
            q = deque()
            q.append((i, j))
            visited[i][j] = True 
            while q:
                r, c = q.popleft()
                for dr, dc in direction:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < row and 0 <= nc < col and 
                    grid[nr][nc] == '1' and not visited[nr][nc]):
                        q.append((nr, nc))
                        visited[nr][nc] = True   

        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1' and not visited[i][j]:
                    bfs(i, j)
                    island += 1
        return island