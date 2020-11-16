class Solution:
    import heapq

    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        temp = sorted(intervals, key=lambda x: x[0])

        heap = []
        heapq.heappush(heap, temp[0][1])

        for start, end in temp[1:]:
            is_free = heap[0] <= start
            if is_free:
                heapq.heappop(heap)

            heapq.heappush(heap, end)

        return len(heap)
