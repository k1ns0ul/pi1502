import sys

class Solution:
    def solve(self):
        n = int(sys.stdin.read())
        print(pow(n, n, 10))

if __name__ == '__main__':
    Solution().solve()