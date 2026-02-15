import sys

class Solution:
    def solve(self):
        input = sys.stdin.readline
        n, m = map(int, input().split())
        A = input().strip()
        B = input().strip()
        
        diff = 0
        for i in range(m):
            if A[i] != B[i]:
                diff += 1
        
        result = diff
        
        for i in range(1, n - m + 1):
            if A[i - 1] != B[0]:
                diff -= 1
            if A[i + m - 1] != B[m - 1]:
                diff += 1
            
            if diff < result:
                result = diff
        
        print(result)

if __name__ == "__main__":
    Solution().solve()