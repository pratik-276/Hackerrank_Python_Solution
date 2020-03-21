if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    listy = list(set(arr))
    listy.sort()
    print(listy[len(listy)-2])
