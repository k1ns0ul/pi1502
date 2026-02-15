import sys

try:
    sys.set_int_max_str_digits(0)
except AttributeError:
    pass

class solution:
    def solve(self):

        input_data = sys.stdin.read().split()
        
        if not input_data:
            return

        n = int(input_data[0])
        m = int(input_data[1])
        a = input_data[2]
        b = input_data[3]

        prefix_a = [0] * (n + 1)
        cnt = 0
        for i, c in enumerate(a):
            if c == '1':
                cnt += 1
            prefix_a[i + 1] = cnt
            
        ones_b = b.count('1')

        lookup = {'0': '000000', '1': '000001'}
        
        hex_a = "".join([lookup[c] for c in reversed(a)])
        num_a = int(hex_a, 16)
        
        hex_b = "".join([lookup[c] for c in b])
        num_b = int(hex_b, 16)
        
        res = num_a * num_b
        
        res_bytes = res.to_bytes((res.bit_length() + 7) // 8, 'little')
        len_bytes = len(res_bytes)
        
        min_dist = m
        
        for k in range(n - m + 1):

            byte_idx = (m - 1 + k) * 3

            if byte_idx + 2 < len_bytes:
                overlap = res_bytes[byte_idx] | (res_bytes[byte_idx+1] << 8) | (res_bytes[byte_idx+2] << 16)
            else:
                overlap = 0

            curr_ones_a = prefix_a[k + m] - prefix_a[k]
            dist = curr_ones_a + ones_b - 2 * overlap
            
            if dist < min_dist:
                min_dist = dist
                
        print(min_dist)

if __name__ == "__main__":
    solution().solve()