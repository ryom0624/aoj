n = int(input())
l = input().split()
l2 = l.copy()


# def isStable(inn, out):
#     print(inn, out)
#     n = len(inn)
#     for i in range(n):
#         for j in range(i+1, n):
#             for a in range(n):
#                 for b in range(a+1, n):
#                     if inn[i][1:] == out[j][1:] and inn[i] == out[b] and inn[j] == out[a]:
#                         print("Unstable")
#                         return
#     print("Stable")
#     return
                    

'''
Bubble sort
H4 C9 S4 D2 C3

H4 C9 S4 D2 C3
H4 C9 D2 S4 C3
H4 D2 C9 S4 C3
D2 H4 C9 S4 C3
D2 H4 C9 C3 S4
D2 H4 C3 C9 S4
D2 C3 H4 C9 S4
D2 C3 H4 S4 C9 
'''

flag = True
while(flag):
    flag = False
    for i in range(n-1, 0, -1):
        
        if(l[i][1:] < l[i-1][1:]):
            l[i], l[i-1] = l[i-1], l[i]
            flag = True
            # print(l)

print(*l)
print("Stable")


'''
Selection sort
H4 C9 S4 D2 C3

H4 C9 S4 D2 C3
D2 C9 S4 H4 C3
D2 C3 S4 H4 C9
D2 C3 S4 H4 C9
'''

for i in range(n):
    minj = i

    for j in range(i+1, n):

        if(l2[j][1:] < l2[minj][1:]):
            minj = j

    l2[i] , l2[minj] = l2[minj], l2[i]
    # print(l2)


print(*l2)
print("Stable") if l == l2 else print("Unstable")













