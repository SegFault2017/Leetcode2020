class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        # sort by starting time
        if not intervals:
            return True
        n = len(intervals)
        temp = sorted(intervals, key=lambda x: x[0])
        prev = temp[0]
        for i in range(n-1):
            current_start = temp[i+1][0]
            prev_end = prev[1]
            if current_start < prev_end:
                return False
            prev = temp[i+1]
        return True
