#num, divisor = map(int, input().split("/"))
num, divisor = map(int, "1/29".split("/"))

if num%divisor == 0:
    print(num//divisor)
else:
    remainder = []
    i = num%divisor
    result = ""
    while i not in remainder and i != 0:
        remainder.append(i)
        result += str(i*10//divisor)
        i = i*10%divisor
    
    if remainder.count(i) >= 1:
        x = remainder.index(i)
        print(f"{num//divisor},{result[:x]}({result[x:]})") 
        #print(len(result)-x) # how often does it repeat?
    else:
        print(f"{num//divisor},{result}")