"""
Design and implement a HitCounter class that records events (hits) at given timestamps (in seconds). You must provide:
record_hit(timestamp_in_seconds) to log an event.
get_hits_in_last_300_seconds(current_time) to return how many hits happened in the last 300 seconds (5 minutes) from current_time.
"""

from collections import deque


class HitCounter:
    def __init__(self):
        self.hits = deque()
        self.window_size = 300

    def record_hit(self, timestamp):
        self.hits.append(timestamp)

    def get_hits_in_last_300_seconds(self, current_time):
        while self.hits and self.hits[0] <= (current_time - self.window_size):
            self.hits.popleft()
        return len(self.hits)



if __name__ == "__main__":
    hc = HitCounter()

    hc.record_hit(10)
    hc.record_hit(200)
    hc.record_hit(300)
    hc.record_hit(550)

    print(hc.get_hits_in_last_300_seconds(320))
    print(hc.get_hits_in_last_300_seconds(600))
