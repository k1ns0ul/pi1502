class solution:
    def solve(self):
        count = 0
        for i in range(256):
            f = [(i >> bit) & 1 for bit in range(8)]
            
            is_monotone = True
            for u in range(8):
                for v in range(u + 1, 8):
                    if (u & v) == u:
                        if f[u] > f[v]:
                            is_monotone = False
                            break
                if not is_monotone:
                    break
            
            if not is_monotone:
                continue
                
            is_self_dual = True
            for u in range(8):
                if f[u] == f[u ^ 7]:
                    is_self_dual = False
                    break
            
            if is_self_dual:
                count += 1
                
        print(count)

if __name__ == '__main__':
    solution().solve()