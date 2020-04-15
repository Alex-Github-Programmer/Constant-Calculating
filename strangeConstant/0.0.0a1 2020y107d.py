import fractions
k = int(1e256)
K = k * k
def sqrt(x):
    a = fractions.Fraction(1)
    b = 0
    while a != b:
        b = a
        a = (a + x / a) / 2
        a = a.limit_denominator(k)
    return a
s = 0
a = fractions.Fraction(2)
while a != 1:
    s += a - 1
    a = sqrt(a)
    s.limit_denominator(K)
print('\n'.join((str(s), str(float(s)))), file = open('resultfrac3.txt', 'w'))
