from typing import List


def countSawSubarrays(arr: List[int]) -> int:
    n = len(arr)
    count = [0] * n  # each element represents the size of the sawtooth subarray
    total = 0
    if n == 0 or n == 1:
        return n

    if n == 2:
        return 1 if (arr[0] % 2 != arr[1] % 2) else 0

    if arr[0] > arr[1] or arr[1] > arr[0]:
        count[1] = 2

    for i in range(2, n):
        if ((arr[i-2] < arr[i-1] and arr[i-1] > arr[i]) or (arr[i-2] > arr[i-1] and arr[i-1] < arr[i])):
            if i == 2:
                count[i] = count[i-2] + 3
            else:
                count[i] = count[i-2] + 2
        elif arr[i-1] > arr[i] or arr[i] > arr[i-1]:
            count[i] = 2

    for size in count:
        if size > 0:
            total += size-1
    return total


if __name__ == "__main__":
    arr = [9, 8, 7, 6, 5]
    print(countSawSubarrays(arr))
