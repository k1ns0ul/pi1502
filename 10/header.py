import sys

class Solution:
    def solve(self):
        input = sys.stdin.readline
        n, m = map(int, input().split())
        A = input().strip()
        B = input().strip()
        B_inv = ''.join('1' if c == '0' else '0' for c in B)
        mod = 1000000007
        base = 91138233
        pow_base = [1] * (n + 1)
        for i in range(1, n + 1):
            pow_base[i] = pow_base[i - 1] * base % mod
        pref_A = [0] * (n + 1)
        for i in range(n):
            pref_A[i + 1] = (pref_A[i] * base + (ord(A[i]) - 48)) % mod
        pref_B = [0] * (m + 1)
        pref_B_inv = [0] * (m + 1)
        for i in range(m):
            pref_B[i + 1] = (pref_B[i] * base + (ord(B[i]) - 48)) % mod
            pref_B_inv[i + 1] = (pref_B_inv[i] * base + (ord(B_inv[i]) - 48)) % mod
        hash_B = pref_B[m]
        hash_B_inv = pref_B_inv[m]
        result = m
        for i in range(n - m + 1):
            cur_hash = (pref_A[i + m] - pref_A[i] * pow_base[m]) % mod
            if cur_hash == hash_B:
                print(0)
                return
            if cur_hash == hash_B_inv:
                result = min(result, m)
                continue
            l = 0
            r = m
            while l < r:
                mid = (l + r) // 2
                hash_sub = (pref_A[i + mid + 1] - pref_A[i] * pow_base[mid + 1]) % mod
                hash_b = pref_B[mid + 1]
                if hash_sub == hash_b:
                    l = mid + 1
                else:
                    r = mid
            mismatches = 0
            start = i
            for j in range(m):
                if A[start + j] != B[j]:
                    mismatches += 1
            if mismatches < result:
                result = mismatches
        print(result)

if __name__ == "__main__":
    Solution().solve()