
n = int(input())
l = list(map(int, input().split()))

'''
5 6 4 2 1 3

1 6 4 2 5 3
1 2 4 6 5 3
1 2 3 6 5 4
1 2 3 4 5 6
'''


c = 0
for i in range(n-1):
    minj = i
    for j in range(i, n):
        if l[j] < l[minj]:
            minj = j

    # print(i, l[i], minj, l[minj])

    if l[i] != l[minj]:
        l[i], l[minj] = l[minj], l[i]
        c += 1
        # print(l)


print(*l)
print(c)
