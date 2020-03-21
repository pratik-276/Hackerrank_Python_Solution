from collections import Counter
number = int(input())

shoe_size = Counter(map(int, input().split()))

buy_num = int(input())

income = 0
for i in range(buy_num):
    order = list(map(int,input().split()))
    if shoe_size[order[0]]:
        income += order[1]
        shoe_size[order[0]] -= 1

print(income)
