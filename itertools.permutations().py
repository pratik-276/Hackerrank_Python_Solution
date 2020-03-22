from itertools import permutations
string, num = input().split()
num = int(num)
lst = list(string)
lst = sorted(lst)

lst1 = list(permutations(lst,num))
joined = list(map("".join,lst1))
for i in joined:
    print(i)
