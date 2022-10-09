import math

n = int(input())
l = [int(input()) for _ in range(n)]

c = 0
for i in l:
    if i == 1: continue
    if i == 2 or i == 3:
        c += 1
        continue
    if i % 2 == 0:
        continue

    # Fermat’s little theorem
    if pow(2, i - 1, i) == 1:
        c += 1

    # isPrime = False
    # for j in range(3, int(math.sqrt(i))+1, 2):
    #     print(i, j)
    #     if i % j == 0:
    #         isPrime = True
    # if not isPrime:
    #     c+= 1
        
print(c)

