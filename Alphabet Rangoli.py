def print_rangoli(s):
    wid = 4*s - 3
    for i in range(1,s+1):
        for j in range(1, wid+1):
            flag = 0
            for k in range(1,s+1):
                if (j<=2*s-1 and j is 2*s-2*i+2*k-1) or (j>2*s-1 and j is 2*s+2*i-2*k-1):
                    print(chr(97+s-k),end='')
                    flag = 1
            if flag is 0:
                print('-',end='')
        print('')
    for i in range(1,s):
        for j in range(1, wid+1):
            flag = 0
            for k in range(1,s+1):
                if (j<=2*s-1 and j is 2*i+2*k-1) or (j>2*s-1 and j is wid-2*i-2*(k-1)):
                    print(chr(97+s-k),end='')
                    flag = 1
            if flag is 0:
                print('-',end='')
        print('')

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
