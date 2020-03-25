nm = list(map(int,input().split()))
n = nm[0]
m = nm[1]

from collections import defaultdict
d = defaultdict(list)

mlst = []

for i in range(n):
    d[input()].append(i+1)
for i in range(m):
    mlst.append(input())

for i in range(m):
    if mlst[i] in d:
        print(" ".join(map(str,d[mlst[i]])))
    else:
        print(-1)
