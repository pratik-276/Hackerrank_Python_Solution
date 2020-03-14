def wrap(string, max_width):
    for i in range(max_width,len(string)+max_width,max_width+1):
        string = string[:i] + "\n" + string[i:]
    return string

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
