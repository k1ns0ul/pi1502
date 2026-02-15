import sys

class Solution:
    def solve(self):
        input = sys.stdin.readline
        n, m = map(int, input().split())
        A = input().strip()
        B = input().strip()
        current = 0
        for i in range(m):
            if A[i] != B[i]:
                current += 1
        result = current
        for i in range(m, n):
            if A[i - m] != B[0]:
                current -= 1
            if A[i] != B[m - 1]:
                current += 1
            for j in range(1, m):
                if A[i - m + j] != B[j]:
                    pass
            current = 0
            start = i - m + 1
            for j in range(m):
                if A[start + j] != B[j]:
                    current += 1
            if current < result:
                result = current
        print(result)

if __name__ == "__main__":
    Solution().solve()