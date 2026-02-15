import sys

class solution:
    def solve(self):
        input_data = sys.stdin.read().split()
        if not input_data:
            return
        
        iterator = iter(input_data)
        try:
            n = int(next(iterator))
            m = int(next(iterator))
            a_str = next(iterator)
            b_str = next(iterator)
        except StopIteration:
            return

        ones_b = b_str.count('1')
        
        p = [0] * (n + 1)
        curr = 0
        for i in range(n):
            if a_str[i] == '1':
                curr += 1
            p[i+1] = curr

        ba_a = bytearray(n * 3)
        for i in range(n):
            if a_str[i] == '1':
                ba_a[i * 3] = 1
        
        ba_b = bytearray(m * 3)
        for i in range(m):
            if b_str[i] == '1':
                idx = (m - 1 - i) * 3
                ba_b[idx] = 1
        
        num_a = int.from_bytes(ba_a, 'little')
        num_b = int.from_bytes(ba_b, 'little')
        
        prod = num_a * num_b
        
        total_bytes = (prod.bit_length() + 7) // 8
        res_ba = prod.to_bytes(total_bytes, 'little')
        
        limit = len(res_ba)
        min_dist = m + 1
        
        for i in range(n - m + 1):
            block_idx = i + m - 1
            offset = block_idx * 3
            
            intersect = 0
            if offset + 3 <= limit:
                intersect = res_ba[offset] | (res_ba[offset+1] << 8) | (res_ba[offset+2] << 16)
            elif offset < limit:
                intersect = int.from_bytes(res_ba[offset:], 'little')
            
            ones_sub_a = p[i + m] - p[i]
            dist = ones_sub_a + ones_b - 2 * intersect
            
            if dist < min_dist:
                min_dist = dist
        
        print(min_dist)

if __name__ == '__main__':
    solution().solve()