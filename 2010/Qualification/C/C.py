import sys
T = input()
for t in range(1, T + 1):
    d = {}
    sys.stdout.write('Case #%d: ' % t)
    R, k, N = map(int, raw_input().split())
    g = map(int, raw_input().split())
    offset = 0
    if sum(g) <= k:
        print R * sum(g)
    else:
        d = {}
        earn = [0] * N
        next = [0] * N
        on_board = 0
        end = 0
        for i in range(N):
            while on_board + g[end] <= k:
                on_board += g[end]
                end = (end + 1) % N
            earn[i] = on_board
            next[i] = end
            on_board -= g[i]
        ans = 0
        cur = 0
        i = 0
        loop = False
        while i < R:
            if cur in d and not loop:
                loop = True
                ediff = ans - d[cur][0]
                idiff = i - d[cur][1]
                ans += ediff * ((R - i) / idiff)
                i = R - ((R - i) % idiff)
            if i == R:
                break
            d[cur] = (ans, i)
            ans += earn[cur]
            cur = next[cur]
            i += 1
        print ans
