import sys

C = input()
def gcd(a, b):
    if b == 0:
        return a
    while a % b != 0:
        a, b = b, a % b
    return b

for case in range(C):
    sys.stdout.write('Case #%d: ' % (case + 1))
    t = map(int, raw_input().split())
    N, t = t[0], t[1:]
    ans = 0
    for i in range(N - 1):
        ans = gcd(ans, abs(t[i + 1] - t[i]))
    out = ans - t[0] % ans
    if out == ans:
        print 0
    else:
        print out
