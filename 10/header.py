import sys

class Solution:
    def solve(self):
        input = sys.stdin.readline
        n, m = map(int, input().split())
        A = input().strip()
        B = input().strip()
        
        if m == 1:
            if B[0] in A:
                print(0)
            else:
                print(1)
            return
        
        base = 91138233
        mod = (1 << 64)
        
        pow_base = [1] * (n + 1)
        for i in range(1, n + 1):
            pow_base[i] = (pow_base[i - 1] * base) & (mod - 1)
        
        prefA = [0] * (n + 1)
        for i in range(n):
            prefA[i + 1] = (prefA[i] * base + (ord(A[i]) - 47)) & (mod - 1)
        
        prefB = [0] * (m + 1)
        for i in range(m):
            prefB[i + 1] = (prefB[i] * base + (ord(B[i]) - 47)) & (mod - 1)
        
        hashB = prefB[m]
        
        def get_hash(l, r):
            return (prefA[r] - prefA[l] * pow_base[r - l]) & (mod - 1)
        
        result = m
        
        for i in range(n - m + 1):
            if get_hash(i, i + m) == hashB:
                print(0)
                return
        
        diff = 0
        for j in range(m):
            if A[j] != B[j]:
                diff += 1
        result = diff
        
        for i in range(1, n - m + 1):
            diff = 0
            for j in range(m):
                if A[i + j] != B[j]:
                    diff += 1
                    if diff >= result:
                        break
            if diff < result:
                result = diff
        
        print(result)

if __name__ == "__main__":
    Solution().solve()