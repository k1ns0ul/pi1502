class Solution:
    def solve(self):
        rtt_sec = 0.12
        total_segments = 767
        loss_segment = 512
        
        cwnd = 1
        ssthresh = float('inf')
        sent_segments = 0
        rtt_count = 0
        loss_processed = False
        
        while sent_segments < total_segments:
            rtt_count += 1
            
            if not loss_processed and sent_segments + cwnd >= loss_segment:
                sent_segments = loss_segment - 1
                ssthresh = max(1, cwnd // 2)
                cwnd = 1
                loss_processed = True
                
                rtt_count += 1
                sent_segments += 1
                continue
            
            can_send = min(cwnd, total_segments - sent_segments)
            sent_segments += can_send
            
            if cwnd < ssthresh:
                cwnd *= 2
            else:
                cwnd += 1
                
        total_time = rtt_count * rtt_sec
        
        options = [1.6, 2.2, 9.6, 3.1, 2.4, 3.0]
        closest = min(options, key=lambda x: abs(x - total_time))
        
        print(f"{str(closest).replace('.', ',')} секунды")

Solution().solve()