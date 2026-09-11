import numpy

n, m = map(int, input().split())

a = []
b = []

for i in range(n):
    x = list(map(int, input().split()))
    a.append(x)

for i in range(n):
    x = list(map(int, input().split()))
    b.append(x)

a = numpy.array(a)
b = numpy.array(b)

print(a + b)
print(a - b)
print(a * b)
print(a // b)
print(a % b)
print(a ** b)
