from math import gcd
with open('exp10.txt') as file:
    a = int(file.readline())
    print(0.0)
    b = int(file.readline())
    print(0.1)
    n = int(file.readline())
    print(0.2)
    k = int(file.readline())
    print(0.3)
    print(n, k)
for i in range(n, n + k):
    a *= i
    a += 1
    b *= i
    if i % 1000 == 0:
        print(str((i - n) * 100 / k) + '%')
print(1)
m = gcd(a, b)
print(2.0)
a //= m
print(2.1)
b //= m
print(2.2)
print('%d\n%d\n%d\n%d' % (a, b, n + k, k), file = open('exp11.txt', 'w'))
print(3)
