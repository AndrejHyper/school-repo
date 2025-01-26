from math import sqrt
from datetime import datetime
import os

start = 0
end = 0
number = int(input("number: "))

start = datetime.now()
i = 3
numbers = 0
if number >= 1: print(str(2)); numbers+=1
while numbers != number:
    max_num = int(sqrt(i))
    prime = True
    for j in range(3, max_num+1, 2):
        if i%j == 0:
            prime = False
            break
    if prime:
        print(str(i),end=" ")
        numbers += 1
    i+=2

end_time = datetime.now()
print('Duration: {}'.format(end_time - start))
print("done")