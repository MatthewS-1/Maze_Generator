import pygame
import random
pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)


def create_grid(rows):
    grid = [[[0, 0, 0, 0] for _ in range(rows)] for _ in range(rows)]  # left right up down; 1 = clear ; 0 = blocked
    return grid


def draw_grid(display, grid):
    # grid thickness = 2
    width, height = (pygame.display.get_surface().get_size())
    width, height = width // rows, height // rows
    for y in range(rows):
        for x in range(rows):
            pygame.draw.rect(display, red, (x * width, y * height, width, height), 2)


def update_grid(display, grid):
    width, height = (pygame.display.get_surface().get_size())
    width, height = width // rows, height // rows

    def calc_center(y, x):
        center = (int((.5 + x) * width), int((.5 + y) * height))
        return center

    for y in range(rows):
        for x in range(rows):
            arr = grid[y][x]
            if arr[0] == 1:
                left_center = calc_center(y, x - 1)
                pygame.draw.rect(display, black, (left_center[0], left_center[1], width, 1), width // 2)
            if arr[1] == 1:
                center = calc_center(y, x)
                pygame.draw.rect(display, black, (center[0], center[1], width, 1), width // 2)
            if arr[2] == 1:
                upper_center = calc_center(y - 1, x)
                pygame.draw.rect(display, black, (upper_center[0], upper_center[1], 1, height), height // 2)
            if arr[3] == 1:
                center = calc_center(y, x)
                pygame.draw.rect(display, black, (center[0], center[1], 1, height), height // 2)


def generate_maze(grid):
    visited = [[False for _ in range(rows)] for _ in range(rows)]

    def get_children(y, x):
        children = []
        if not x == 0:
            children.append((y, x - 1))
        if not x == rows - 1:
            children.append((y, x + 1))
        if not y == 0:
            children.append((y - 1, x))
        if not y == rows - 1:
            children.append((y + 1, x))
        return children

    def update_grid(y1, x1, y2, x2):
        arr = grid[y1][x1]
        arr2 = grid[y2][x2]
        if y1 == y2 + 1:
            arr[2] = 1
            arr2[3] = 1
        if y1 == y2 - 1:
            arr[3] = 1
            arr2[2] = 1
        if x1 == x2 - 1:
            arr[1] = 1
            arr2[0] = 1
        if x1 == x2 + 1:
            arr[0] = 1
            arr2[1] = 1
    def randomized_dfs(y, x):
        random.seed(random.randint(0, 10 ** 10))
        if x == rows - 1 and y == rows - 1:
            return
        visited[y][x] = True
        children = get_children(y, x)
        random.shuffle(children)
        for child in children:
            if not visited[child[0]][child[1]]:
                visited[child[0]][child[1]] = True
                update_grid(y, x, child[0], child[1])
                randomized_dfs(child[0], child[1])
    randomized_dfs(0, 0)
    return grid

rows = 15#int(input("how wide would you like the grid to be?"))
grid = create_grid(rows)

def main():
    display = pygame.display.set_mode((1000, 1000))
    draw_grid(display, grid)
    generate_maze(grid)
    update_grid(display, grid)
    try:
        for y in grid:
            print(y.index([0,0,0,0]))
    except:
        print(grid)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pygame.display.flip()
if __name__ == '__main__':
    main()
