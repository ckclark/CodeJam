from math import sqrt
T = input()
for case in range(1, T + 1):
    L, P, C = map(int, raw_input().split())
    ans = 0
    while C * L < P:
        ans += 1
        C *= C
    print 'Case #%s: %s' % (case, ans)
