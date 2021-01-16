import heapq


def find3LargestNumbers(arr: List[int]) -> List[int]:
    """
    Strategy 1: Linear scan
    Runtime:O(n), where n is the number of elements in arr
    Space:O(1)

    arr: [List[int]] an arrary of integers

    return [List[int]] 3 largest elements in arr
    """

    n = len(arr)
    if n < 3:
        return None

    pass
