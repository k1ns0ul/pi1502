import math

class solution:
    def solve(self):
        n = 3
        while True:
            total_cycles = 0
            for k in range(3, n + 1):
                total_cycles += math.comb(n, k) * math.factorial(k - 1) // 2
            
            if total_cycles >= 2026:
                print(n)
                return
            n += 1

solution().solve()