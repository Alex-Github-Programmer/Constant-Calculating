import pickle
with open('exp7.txt') as file:
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
    if i % (k // 10000) == 0:
        print(str((i - n) * 100 / k) + '%')
print(1)
pickle.dump([a, b, n, k], open('exp8.txt', 'wb'))
#print('%d\n%d\n%d\n%d' % (a, b, n + k, k), file = open('exp8.txt', 'w'))
print(2)
