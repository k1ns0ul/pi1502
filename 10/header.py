import sys

class Solution:
    def solve(self):
        input = sys.stdin.readline
        n, m = map(int, input().split())
        A = input().strip()
        B = input().strip()

        b = 0
        for i in range(m):
            if B[i] == '1':
                b |= 1 << i

        window = 0
        for i in range(m):
            if A[i] == '1':
                window |= 1 << i

        def bits(x):
            return bin(x).count("1")

        ans = bits(window ^ b)
        mask = (1 << m) - 1

        for i in range(m, n):
            window >>= 1
            if A[i] == '1':
                window |= 1 << (m - 1)
            window &= mask
            cur = bits(window ^ b)
            if cur < ans:
                ans = cur

        print(ans)

if __name__ == "__main__":
    Solution().solve()
