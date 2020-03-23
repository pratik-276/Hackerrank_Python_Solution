def average(array):
    sety = list(set(array))
    return sum(sety)/len(sety)

if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    result = average(arr)
    print result
