
n = int(input())

max = -10**18
min = 10**18


for i in range(n):
    r = int(input())
    if max < r - min:
        max = r - min
    if min > r:
        min = r
print(max)


'''
n^3

5             []
5 3           [3-5]  => -2
5 3 1         [3-5 / 1-5 / 1-3]  => -2
5 3 1 3       [3-5 / 1-5 / 3-5 / 1-3 / 3-3 / 3-1]  => 2
5 3 1 3 4     [3-5 / 1-5 / 3-5 / 4-5 / 1-3 / 3-3 / 4-3 / 3-1 / 4-1 / 4-3] => 3 
5 3 1 3 4 3   [3-5 / 1-5 / 3-5 / 4-5 / 3-5 / 1-3 / 3-3 / 4-3 / 3-3 / 3-1 / 4-1 / 4-3 / 3-3 / 3-4]

i  k-j
0:
1: 1-0
2: 1-0/2-0/1-0
3: 1-0/2-0/3-0/2-1/3-1/3-2
4: 1-0/2-0/3-0/4-0/2-1/3-1/4-1/3-2/4-2/4-3

4 3 29 22      [3-4/29-4/22-4 / 29-3/22-3 / 22-29]
'''

# n = int(input())
# l = [int(input()) for i in range(n)]
# max = 0
# for i in range(n):
#     for j in range(i):
#         for k in range(j+1, i+1):
#             p =  l[k] - l[j]
#             # print(l[k], "-", l[j], "=", p, end=", ")
#             if p > max or (i == 1 and j == 0 and k == 1):
#                 max = p 
#             else: 
#                 max = max
#     # print()

# print(max)
