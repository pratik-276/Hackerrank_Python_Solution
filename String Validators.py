if __name__ == '__main__':
    s = input()
    alphanum = 0
    alpha = 0
    dig = 0
    lower = 0
    upper = 0
    for i in range(len(s)):
        if(s[i].isalnum()):
            alphanum += 1
        if(s[i].isalpha()):
            alpha += 1
        if(s[i].isdigit()):
            dig += 1
        if(s[i].islower()):
            lower += 1
        if(s[i].isupper()):
            upper += 1
    if alphanum > 0:
        print(True)
    else:
        print(False)
    if alpha > 0:
        print(True)
    else:
        print(False)
    if dig > 0:
        print(True)
    else:
        print(False)
    if lower > 0:
        print(True)
    else:
        print(False)
    if upper > 0:
        print(True)
    else:
        print(False)
