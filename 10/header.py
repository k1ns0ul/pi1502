import sys

class solution:
    def solve(self):
        input_data = sys.stdin.read().split()
        if not input_data:
            return

        n = int(input_data[0])
        m = int(input_data[1])
        a = input_data[2]
        b = input_data[3]

        block_size = 21
        pad = 20

        trans_table = str.maketrans({
            '1': '0' * pad + '1',
            '0': '0' * block_size
        })

        val_a = int(a[::-1].translate(trans_table), 2)
        val_b = int(b.translate(trans_table), 2)

        prod = val_a * val_b
        
        res_str = bin(prod)[2:]
        len_res = len(res_str)

        prefix_ones = [0] * (n + 1)
        current_ones = 0
        for i in range(n):
            if a[i] == '1':
                current_ones += 1
            prefix_ones[i+1] = current_ones

        ones_b = b.count('1')
        min_dist = m + 1

        for k in range(n - m + 1):
            shift = (k + m - 1) * block_size
            end_idx = len_res - shift
            start_idx = end_idx - pad
            
            matches = 0
            if end_idx > 0:
                actual_start = 0 if start_idx < 0 else start_idx
                if actual_start < end_idx:
                    matches = int(res_str[actual_start:end_idx], 2)

            dist = (prefix_ones[k + m] - prefix_ones[k]) + ones_b - 2 * matches
            if dist < min_dist:
                min_dist = dist

        print(min_dist)

if __name__ == '__main__':
    solution().solve()