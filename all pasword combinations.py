letters = ["a","b","c","d"]
lenght = 8
count = 0

def combinations(len, password):
    global count
    if len == 0:
        print(password)
        count += 1
        return
    
    for i in letters:
        combinations(len-1, password + i)
         
        

combinations(lenght, "")
print(count)