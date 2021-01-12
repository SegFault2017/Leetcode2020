from typing import List


def waterArea(heights: List[int]) -> int:
    n = len(heights)
    area = 0
    for i in range(1, n-1):
        left = heights[i]
        for j in range(i):
            left = max(left, heights[j])
        right = heights[i]
        for j in range(i+1, n):
            right = max(right, heights[j])

        area += min(left, right) - heights[i]
    return area


if __name__ == "__main__":
    heights = [0, 8, 0, 0, 5, 0, 0, 10, 0, 0, 1, 1, 0, 3]
    print(waterArea(heights))
