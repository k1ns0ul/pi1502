import sys
import numpy as np
from numpy.fft import rfft, irfft

class Solution:
    def solve(self):
        input_data = sys.stdin.buffer.read().split()
        n = int(input_data[0])
        m = int(input_data[1])
        A = input_data[2].decode()
        B = input_data[3].decode()

        a = np.array([int(c) for c in A], dtype=np.float64)
        b = np.array([int(c) for c in B], dtype=np.float64)

        b_rev = b[::-1]

        size = 1
        while size < n + m:
            size <<= 1

        fa = rfft(a, size)
        fb_rev = rfft(b_rev, size)
        conv_ab = irfft(fa * fb_rev, size)

        a_inv = 1.0 - a
        fa_inv = rfft(a_inv, size)
        b_inv = 1.0 - b
        b_inv_rev = b_inv[::-1]
        fb_inv_rev = rfft(b_inv_rev, size)
        conv_ab_inv = irfft(fa_inv * fb_inv_rev, size)

        num_positions = n - m + 1
        matches = np.round(conv_ab[m-1:m-1+num_positions] + conv_ab_inv[m-1:m-1+num_positions]).astype(np.int64)

        min_hamming = m - int(np.max(matches))
        print(min_hamming)

Solution().solve()