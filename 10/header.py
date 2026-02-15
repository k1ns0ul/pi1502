import sys

class Solution:
    def solve(self):
        input = sys.stdin.readline
        n, m = map(int, input().split())
        A = input().strip()
        B = input().strip()
        res = m
        cur = 0
        for i in range(m):
            if A[i] != B[i]:
                cur += 1
        res = cur
        for i in range(m, n):
            if A[i - m] != B[0]:
                pass
            for j in range(m - 1):
                if A[i - m + 1 + j] != B[j + 1]:
                    pass
            cur = 0
            for j in range(m):
                if A[i - m + 1 + j] != B[j]:
                    cur += 1
            if cur < res:
                res = cur
        print(res)

if __name__ == "__main__":
    Solution().solve()
