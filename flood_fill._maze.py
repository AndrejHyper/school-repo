from re import S
from time import sleep

from ollama import generate
import maze_gen

maze = maze_gen.generate_maze(0, 0)

def print_maze():
    print(" " + "_" * (len(maze[0]) * 2 - 1))
    for y in range(len(maze)):
        row = "|"
        for x in range(len(maze[0])):
            row += " " if not maze[y][x]["S"] else "_"
            row += "|" if maze[y][x]["E"] else " "
        print(row)

print_maze()

width = 16
height = 16

goal = [[len(maze[0])/2 - 1, len(maze)/2 - 1],
        [len(maze[0])/2 - 1, len(maze)/2],
        [len(maze[0])/2, len(maze)/2 - 1],
        [len(maze[0])/2, len(maze)/2]]

cell = {
    "N": False,
    "E": False,
    "S": False,
    "W": False,
    "visited": False
}

mice_maze = [[cell.copy() for _ in range(len(maze[0]))] for _ in range(len(maze))]
flood_maze = [[9999 for _ in range(len(maze[0]))] for _ in range(len(maze))]

def flood_fill(x, y, distance):
    if 0 <= x < len(maze[0]) and 0 <= y < len(maze):
        if distance >= flood_maze[y][x]:
            return
        flood_maze[y][x] = distance
        if not mice_maze[y][x]["N"]:
            flood_fill(x, y-1, distance + 1)
        if not mice_maze[y][x]["S"]:
            flood_fill(x, y+1, distance + 1)
        if not mice_maze[y][x]["W"]:
            flood_fill(x-1, y, distance + 1)
        if not mice_maze[y][x]["E"]:
            flood_fill(x+1, y, distance + 1)

def flood():
    for y in range(len(flood_maze)):
        for x in range(len(flood_maze[0])):
            flood_maze[y][x] = 9999
            
    for g in goal:
        flood_fill(int(g[0]), int(g[1]), 0)
    
    #print("Flood Maze:")
    #for row in flood_maze:
    #    print(row)

def update_cell(x, y):
    mice_maze[y][x] = maze[y][x]
    if 0 <= y-1 and mice_maze[y][x]["N"]:
        mice_maze[y-1][x]["S"] = True
    if y+1 < height and mice_maze[y][x]["S"]:
        mice_maze[y+1][x]["N"] = True
    if 0 <= x-1 and mice_maze[y][x]["W"]:
        mice_maze[y][x-1]["E"] = True
    if x+1 < width and mice_maze[y][x]["E"]:
        mice_maze[y][x+1]["W"] = True
        
    mice_maze[y][x]["visited"] = True
    #print(mice_maze[y][x])

DIRS = {
    "N": (0, -1, "S"),
    "E": (1, 0, "W"),
    "S": (0, 1, "N"),
    "W": (-1, 0, "E")
}
steps = 0
def solve(x, y):
    global steps
    steps += 1
    print(f"at ({x}, {y})")
    if [x, y] in goal:
        print(f"Reached goal at ({x}, {y}) in {steps} steps!")
        return
    update_cell(x, y)
    flood()
    #sleep(2)
    lowest_distance = 99999
    lowest_dir = ""
    
    # north
    if y - 1 >= 0 and not mice_maze[y][x]["N"]:
        if flood_maze[y-1][x] < lowest_distance:
            lowest_distance = flood_maze[y-1][x]
            lowest_dir = "N"
    # south
    if y + 1 < height and not mice_maze[y][x]["S"]:
        if flood_maze[y+1][x] < lowest_distance:
            lowest_distance = flood_maze[y+1][x]
            lowest_dir = "S"
    # west
    if x - 1 >= 0 and not mice_maze[y][x]["W"]:
        if flood_maze[y][x-1] < lowest_distance:
            lowest_distance = flood_maze[y][x-1]
            lowest_dir = "W"
    # east
    if x + 1 < width and not mice_maze[y][x]["E"]:
        if flood_maze[y][x+1] < lowest_distance:
            lowest_distance = flood_maze[y][x+1]
            lowest_dir = "E"
    
    solve(x + DIRS[lowest_dir][0], y + DIRS[lowest_dir][1])

solve(0,0)