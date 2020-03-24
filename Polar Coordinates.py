import cmath

string = input()
comp = complex(string)

polar = cmath.polar(comp)

print(polar[0])
print(polar[1])
