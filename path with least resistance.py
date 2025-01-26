room = [
    [3, 5, 2, 4],
    [6, 8, 1, 3],
    [4, 7, 5, 6],
    [2, 3, 4, 1]
]

def create_resistance_matrix(room):
    resistance_matrix = [[0]*len(room[0]) for _ in range(len(room))]
    for y in range(len(room)):
        for x in range(len(room[0])):
            if y == 0:
                resistance_matrix[0][x] = resistance_matrix[0][x-1] + room[0][x]
            elif x == 0:
                resistance_matrix[y][0] = resistance_matrix[y-1][0] + room[y][0]
            else:
                if resistance_matrix[y][x-1] + room[y][x] > resistance_matrix[y-1][x] + room[y][x]:
                    resistance_matrix[y][x] = resistance_matrix[y-1][x] + room[y][x]
                else:
                    resistance_matrix[y][x] = resistance_matrix[y][x-1] + room[y][x]
    return resistance_matrix

def least_resistance_path(resistance_matrix):
    y = len(resistance_matrix)-1
    x = len(resistance_matrix[0])-1
    path = [y, x]
    while x != 0 or y !=0:
        if resistance_matrix[y][x-1] > resistance_matrix[y-1][x]:
            y-=1
            path.append((y,x))
        else:
            x-=1
            path.append((y,x))

    return(resistance_matrix[-1][-1] ,path[::-1])

least_resistance, path = least_resistance_path(create_resistance_matrix(room)) 
print(least_resistance)
print(path)
print("--------------------------------")

#create_resistance_matrix(room)