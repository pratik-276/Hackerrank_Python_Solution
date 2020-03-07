if __name__ == '__main__':
    student = []
    student1 = []
    score = []
    n = int(input())
    for i in range(n):
        student.append(input())
        score.append(float(input()))
    copy = score
    copy = list(set(copy))
    copy.sort()
    min_two = copy[1]
    for i in range(n):
        if score[i] == min_two:
            student1.append(student[i])
    student1.sort()
    for i in range(len(student1)):
        print(student1[i])
