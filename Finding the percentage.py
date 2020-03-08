if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    for i in student_marks:
        if i == query_name:
            newsum = sum(student_marks[i])
            out = newsum/3
    print("{:.2f}".format(out))
