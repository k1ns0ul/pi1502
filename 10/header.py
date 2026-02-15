import sys

class Solution:
    def solve(self):
        data = sys.stdin.buffer.read().split()
        n = int(data[0])
        m = int(data[1])
        A = data[2].decode()
        B = data[3].decode()

        mask_b = int(B, 2)
        a_bits = int(A, 2)
        mask = (1 << m) - 1
        shift = n - m

        best = m
        for i in range(n - m + 1):
            xor = ((a_bits >> (shift - i)) & mask) ^ mask_b
            h = bin(xor).count('1')
            if h < best:
                best = h
                if best == 0:
                    break

        print(best)

Solution().solve()