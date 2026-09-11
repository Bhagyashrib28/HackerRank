import numpy

n, m = map(int, input().split())

my_array = []

for i in range(n):
    row = list(map(int, input().split()))
    my_array.append(row)

my_array = numpy.array(my_array)

result = numpy.sum(my_array, axis=0)

print(numpy.prod(result))
