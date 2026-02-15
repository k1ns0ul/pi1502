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
            if diff >= result:
                d = 0
                ai = A[i:i + m]
                for j in range(m):
                    if ai[j] != B[j]:
                        d += 1
                        if d >= result:
                            break
                diff = d
            else:
                d = 0
                ai = A[i:i + m]
                for j in range(m):
                    if ai[j] != B[j]:
                        d += 1
                diff = d
            
            if diff < result:
                result = diff
        
        print(result)

if __name__ == "__main__":
    Solution().solve()