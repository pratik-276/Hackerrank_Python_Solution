def count_substring(string, sub_string):
    lst = list(string)
    count = 0
    sublen = len(sub_string)
    for i in range(len(lst)-sublen+1):
        tot = ''
        for j in range(sublen):
            tot += lst[i+j]
        if tot == sub_string:
            count += 1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
