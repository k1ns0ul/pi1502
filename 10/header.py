import sys
import numpy as np

class Solution:
    def solve(self):
        input = sys.stdin.readline
        n, m = map(int, input().split())
        A = input().strip()
        B = input().strip()
        
        a = np.array([int(c) for c in A], dtype=np.float64)
        b = np.array([int(c) for c in B[::-1]], dtype=np.float64)
        
        size = 1
        while size < n + m:
            size <<= 1
        
        fa = np.fft.fft(a, size)
        fb = np.fft.fft(b, size)
        conv1 = np.fft.ifft(fa * fb).real.round().astype(np.int64)
        
        a0 = 1 - a
        b0 = 1 - b
        fa0 = np.fft.fft(a0, size)
        fb0 = np.fft.fft(b0, size)
        conv0 = np.fft.ifft(fa0 * fb0).real.round().astype(np.int64)
        
        max_match = 0
        for i in range(m - 1, n):
            matches = conv1[i] + conv0[i]
            if matches > max_match:
                max_match = matches
        
        print(m - max_match)

if __name__ == "__main__":
    Solution().solve()