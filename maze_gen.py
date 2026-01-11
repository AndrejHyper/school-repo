import random

width = 16
height = 16

#top bottom left right
cell = {
    "N": True,
    "E": True,
    "S": True,
    "W": True,
    "visited": False
}

maze = [[cell.copy() for _ in range(width)] for _ in range(height)]

DIRS = {
    "N": (0, -1, "S"),
    "E": (1, 0, "W"),
    "S": (0, 1, "N"),
    "W": (-1, 0, "E")
}

def generate_maze(x, y):
    maze[y][x]["visited"] = True
    dirs = list(DIRS.keys())
    random.shuffle(dirs)
    
    for direction in dirs:
        dx, dy, oposite = DIRS[direction]
        nx, ny = x + dx, y + dy
        
        if 0 <= nx < width and 0 <= ny < height and not maze[ny][nx]["visited"]:
            maze[y][x][direction] = False
            maze[ny][nx][oposite] = False
            generate_maze(nx, ny)
    return maze

generate_maze(0, 0)

def print_maze():
    print(" " + "_" * (width * 2 - 1))
    for y in range(height):
        row = "|"
        for x in range(width):
            row += " " if not maze[y][x]["S"] else "_"
            row += "|" if maze[y][x]["E"] else " "
        print(row)

#print_maze()
