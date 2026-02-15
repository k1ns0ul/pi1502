import sys
import threading

class Solution:
    def solve(self):
        input = sys.stdin.readline
        n, m = map(int, input().split())
        A = input().strip()
        B = input().strip()

        size = 1
        while size < n + m:
            size <<= 1

        import cmath

        def fft(a, invert):
            n = len(a)
            j = 0
            for i in range(1, n):
                bit = n >> 1
                while j & bit:
                    j ^= bit
                    bit >>= 1
                j |= bit
                if i < j:
                    a[i], a[j] = a[j], a[i]
            length = 2
            while length <= n:
                ang = 2 * cmath.pi / length * (-1 if invert else 1)
                wlen = complex(cmath.cos(ang), cmath.sin(ang))
                for i in range(0, n, length):
                    w = 1+0j
                    half = length >> 1
                    for j in range(i, i + half):
                        u = a[j]
                        v = a[j + half] * w
                        a[j] = u + v
                        a[j + half] = u - v
                        w *= wlen
                length <<= 1
            if invert:
                for i in range(n):
                    a[i] /= n

        def convolution(x, y):
            fa = list(map(complex, x)) + [0j] * (size - len(x))
            fb = list(map(complex, y)) + [0j] * (size - len(y))
            fft(fa, False)
            fft(fb, False)
            for i in range(size):
                fa[i] *= fb[i]
            fft(fa, True)
            return [int(fa[i].real + 0.5) for i in range(n + m - 1)]

        a1 = [1 if c == '1' else 0 for c in A]
        b1 = [1 if c == '1' else 0 for c in B[::-1]]
        a0 = [1 if c == '0' else 0 for c in A]
        b0 = [1 if c == '0' else 0 for c in B[::-1]]

        c1 = convolution(a1, b1)
        c0 = convolution(a0, b0)

        ans = m
        for i in range(m - 1, n):
            matches = c1[i] + c0[i]
            ans = min(ans, m - matches)

        print(ans)

if __name__ == "__main__":
    Solution().solve()
