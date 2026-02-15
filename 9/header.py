class solution:
    def __init__(self):
        import sys
        data = sys.stdin.read().strip().split()
        if not data:
            return
        it = iter(data)
        n = int(next(it))
        reds = []
        blues = []
        sumR = 0
        sumB = 0
        for _ in range(n):
            c = next(it)
            w = int(next(it))
            if c == 'R':
                reds.append(w)
                sumR += w
            else:
                blues.append(w)
                sumB += w
        D = sumR - sumB
        if D > 0:
            weights = reds
            target = D // 2 + 1
        else:
            weights = blues
            D = -D
            target = D // 2 + 1
        total = sum(weights)
        dp = 1
        for w in weights:
            dp |= dp << w
        res = 0
        for s in range(target, total + 1):
            if (dp >> s) & 1:
                res = s
                break
        sys.stdout.write(str(res))

solution()