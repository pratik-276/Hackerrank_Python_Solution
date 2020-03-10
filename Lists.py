if _name_ == '_main_':
    N = int(input())
    l = []
    for i in range(N):
        s = input().split()
        check = s[0]
        other = s[1:]
        if check == 'print':
            print(l)
        else:
            if len(other) == 1:
                eval("l."+check+"("+other[0]+")")
            elif len(other) == 2:
                eval("l."+check+"("+other[0]+","+other[1]+")")
            else:
                eval("l."+check+"()")
