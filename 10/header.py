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
        current_ones = 0
        for i, char in enumerate(a):
            if char == '1':
                current_ones += 1
            prefix_a[i+1] = current_ones
            
        ones_b = b.count('1')

        CHUNK_SIZE = 20
        pad = '0' * (CHUNK_SIZE - 1)
        
        parts_a = [pad + c for c in a[::-1]]
        num_a = int("".join(parts_a), 2)
        
        parts_b = [pad + c for c in b]
        num_b = int("".join(parts_b), 2)
        
        prod = num_a * num_b
        
        res_bin = bin(prod)[2:]
        len_res = len(res_bin)
        
        min_hamming = m
        
        for k in range(n - m + 1):
            p = m - 1 + k
            
            end_idx = len_res - p * CHUNK_SIZE
            start_idx = len_res - (p + 1) * CHUNK_SIZE
            
            overlap = 0
            if end_idx > 0:
                real_start = max(0, start_idx)
                chunk = res_bin[real_start:end_idx]
                if chunk:
                    overlap = int(chunk, 2)
            
            ones_sub_a = prefix_a[k+m] - prefix_a[k]
            
            dist = ones_sub_a + ones_b - 2 * overlap
            
            if dist < min_hamming:
                min_hamming = dist
                
        print(min_hamming)

if __name__ == '__main__':
    solution().solve()