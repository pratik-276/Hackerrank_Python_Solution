from collections import namedtuple

n = int(input()) 
categories = input().split()

grade = namedtuple('Grade', categories)
marks = [int(grade._make(input().split()).MARKS) for _ in range(n)]
print((sum(marks) / len(marks)))
