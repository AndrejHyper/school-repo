#number = int(input("starting number: "))
loop = int(input("starting number: "))

longest_num = 1
longest = 0
iteration = 0
for number in range(1, loop):
    lenght = 0
    iteration += 1
    while number != 1:
        lenght += 1
        if number % 2 == 0:
            number = number/2
        else:
            number = number*3+1
        print(int(number), end=" ")
    if lenght > longest:
        longest = lenght
        longest_num = iteration
    print("")
    print(f"finished loop {int(iteration)}")
    print("---------------------------------------------")
    

print(f"finished")
print(f"longest num {longest_num}")
print(f"longest lenght {longest}")