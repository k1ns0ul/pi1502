import sys
import numpy as np

class solution:
    def solve(self):
        data = sys.stdin.read().split()
        if not data:
            return

        n = int(data[0])
        m = int(data[1])
        s_a = data[2]
        s_b = data[3]

        a = np.frombuffer(s_a.encode(), dtype=np.int8) - 48
        b = np.frombuffer(s_b.encode(), dtype=np.int8) - 48

        size = 1
        while size < n + m:
            size *= 2

        fa = np.fft.rfft(a, size)
        fb = np.fft.rfft(b[::-1], size)
        
        cross_corr = np.fft.irfft(fa * fb, size)
        matches = np.rint(cross_corr[m-1:n]).astype(np.int32)

        pref = np.zeros(n + 1, dtype=np.int32)
        np.cumsum(a, out=pref[1:])
        
        sum_a_windows = pref[m:n+1] - pref[0:n-m+1]
        sum_b = np.sum(b)

        distances = sum_a_windows + sum_b - 2 * matches
        
        print(np.min(distances))

if __name__ == '__main__':
    solution().solve()