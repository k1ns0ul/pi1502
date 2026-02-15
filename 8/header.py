import sys
import math

class solution:
    def solve(self):
        data = sys.stdin.read().split()
        if not data:
            return
        n = int(data[0])
        ans = 0
        for c in range(1, n + 1):
            min_b = math.isqrt((c * c) // 2) + 1
            for b in range(min_b, c + 1):
                min_a = math.isqrt(c * c - b * b) + 1
                ans += b - min_a + 1
        print(ans)

solution().solve()