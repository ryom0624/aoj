'''
挿入ソート
'''
n = int(input())
l = list(map(int, input().split()))

for i in range(len(l)):
    if(i == 0):
        for k in range(len(l)):
            print(l[k], end="") if(len(l)-1 == k) else print(l[k], end=" ")
        print()
        continue
    v = l[i] 
    j = i - 1
    while(j >= 0 and l[j] > v):
        l[j+1] = l[j]
        j -= 1
    l[j+1] = v

    for k in range(len(l)):
        print(l[k], end="") if(len(l)-1 == k) else print(l[k], end=" ")
    print()
