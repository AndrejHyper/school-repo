items = [[20,4],
         [30,6],
         [40,3],
         [50,7],
         [60,5],
         [70,2]
         ]

max_weight = 1+15

def find_solution(items, max_weight):
    dp = [[0]*max_weight for _ in range(len(items)+1)]

    for i in range(len(items)):
        for j in range(max_weight):
            #if j != 0:
                if j >= items[i][-1]:
                    dp[i+1][j] = max(items[i][0] + dp[i][j-items[i][-1] if j-items[i][-1] > 0 else 0], dp[i][j])
                else:
                    dp[i+1][j] = dp[i][j]

    #solution
    x = len(dp[0])-1
    y = len(dp)-1
    used = []
    while dp[y][x] != 0:
        if dp[y-1][x] == dp[y][x]:
            y -= 1
        else:
            used.append(y)
            x -= items[y-1][-1]
            y -= 1
        
    weight = sum([items[i-1][-1] for i in used])

    """
    for _ in dp:
        print(_)
    
    #the slightly cursed print
    print("".join([f"{_}\n" for _ in dp]))
    """
    #print(f"\n {used}")
    #print(weight)
    return dp[-1][-1], used, weight

max, used, weight = find_solution(items, max_weight)

print(f"najväčšia hodnota {max}")
print(f"použité predmety {used}")
print(f"celková hmotnosť {weight}")