t = int(input())
while t:
    a, b = input().split()
    try:
        print(int(a) // int(b))
    except BaseException as e:
        print("Error Code:", e)
    t-=1
