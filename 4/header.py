class Solution:
    def get_result(self):
        base = "тромб"
        words = ["столб", "сталь", "тропа", "клоун", "скраб"]
        
        def jaccard(a, b):
            sa, sb = set(a), set(b)
            return len(sa & sb) / len(sa | sb)
        
        def hamming(a, b):
            return sum(c1 != c2 for c1, c2 in zip(a, b))
        
        def lcs_len(a, b):
            m, n = len(a), len(b)
            dp = [[0] * (n + 1) for _ in range(m + 1)]
            for i in range(1, m + 1):
                for j in range(1, n + 1):
                    if a[i - 1] == b[j - 1]:
                        dp[i][j] = dp[i - 1][j - 1] + 1
                    else:
                        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
            return dp[m][n]
        
        metrics = []
        for word in words:
            j = jaccard(base, word)
            h = hamming(base, word)
            lcs = lcs_len(base, word)
            metrics.append((j, h, lcs))
        
        def rank(values, descending=True):
            indexed = [(i, v) for i, v in enumerate(values)]
            indexed.sort(key=lambda x: x[1], reverse=descending)
            ranks = [0.0] * 5
            i = 0
            while i < 5:
                curr_val = indexed[i][1]
                start = i
                while i < 5 and indexed[i][1] == curr_val:
                    i += 1
                avg_rank = (start + i + 1) / 2.0
                for k in range(start, i):
                    ranks[indexed[k][0]] = avg_rank
            return ranks
        
        rank_j = rank([m[0] for m in metrics], descending=True)
        rank_h = rank([m[1] for m in metrics], descending=False)
        rank_lcs = rank([m[2] for m in metrics], descending=True)
        
        avg_ranks = []
        for i in range(5):
            avg = (rank_j[i] + rank_h[i] + rank_lcs[i]) / 3.0
            avg_ranks.append((avg, i + 1))
        
        avg_ranks.sort()
        return "".join(str(num) for _, num in avg_ranks)

print(Solution().get_result())