def minion_game(string):
    l = len(string)
    v = 'IOEUA'
    s1 = 0
    s2 = 0
    for i in range(l):
        if string[i] in v:
            s1 += l - i
        else:
            s2 += l - i
    if(s1<s2):
        print('Stuart',s2)
    elif(s1>s2):
        print('Kevin',s1)
    else:
        print('Draw')

if __name__ == '__main__':
    s = input()
    minion_game(s)
