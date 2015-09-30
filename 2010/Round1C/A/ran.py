from random import randint
T = 1
print T
N = 1000
print N
A, B = set(), set()
for i in range(N):
    while True:
        a = randint(1, 10000)
        if a not in A:
            A.add(a)
            break
    while True:
        b = randint(1, 10000)
        if b not in B:
            B.add(b)
            break
    print a, b

