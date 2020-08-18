import fractions
k = int(1e256) ** 128
def sqrt(x):
    a = fractions.Fraction(1)
    b = 0
    while a != b:
        b = a
        a = (a + x / a) / 2
        a = a.limit_denominator(k)
    return a
s = 1103
x = sqrt(2) * 2 / 9801
i = 0
a = fractions.Fraction(1)
while a != 0:
    i += 1
    a = a * (4 * i + 1) * (4 * i + 2) * \
        (4 * i + 3) * (i + 1) * 4 / (i ** 4) / 24591257856 \
        / (26390 * i - 25287) * (26390 * i + 1103)
    s += a
    a = a.limit_denominator(k)
    s = s.limit_denominator(k)
s = 1 / (s * x)
print('\n'.join((str(s), str(float(s)))), file = open('pi-6.txt', 'w'))
