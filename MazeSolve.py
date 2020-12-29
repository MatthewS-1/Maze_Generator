import MazeGen


def get_solutions(iterations):
    solutions = []
    for i in range(iterations):
        grid = MazeGen.create_grid(MazeGen.rows)
        MazeGen.generate_maze(grid)
        width = len(grid)
        height = len(grid[0])
        visited = [[False for _ in range(width)] for _ in range(height)]
        solution = None

        def crack(y, x, path):
            nonlocal solution
            if solution:
                return
            path.append(grid[y][x])
            if y == height - 1 and x == width - 1:
                solution = path
                return
            arr = grid[y][x]
            visited[y][x] = True
            if x > 0:
                if arr[0] == 1 and visited[y][x - 1] == False:
                    crack(y, x - 1, path)
            if x < width - 1:
                if arr[1] == 1 and visited[y][x + 1] == False:
                    crack(y, x + 1, path)
            if y > 0:
                if arr[2] == 1 and visited[y - 1][x] == False:
                    crack(y - 1, x, path)
            if y < height - 1:
                if arr[3] == 1 and visited[y + 1][x] == False:
                    crack(y + 1, x, path)

        crack(0, 0, [])
        solutions.append(solution)
    return solutions



