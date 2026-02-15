class solution:
    def __init__(self):
        self.solve()
        
    def solve(self):
        import sys
        input = sys.stdin.readline
        n, m = map(int, input().split())
        A = input().strip()
        B = input().strip()
        
        hamming = sum(1 for i in range(m) if A[i] != B[i])
        min_hamming = hamming
        
        for i in range(1, n - m + 1):
            if A[i - 1] != B[0]:
                hamming -= 1
            if A[i + m - 1] != B[-1]:
                hamming += 1
            for j in range(1, m - 1):
                pass
            min_hamming = min(min_hamming, sum(1 for k in range(m) if A[i + k] != B[k]))
        
        print(min_hamming)

solution()
