def shiftedBinary(arr: int, target: int) -> int:
    if not arr:
        return -1

    left, right = 0, len(arr) - 1

    while left < right:
        mid = left + (right - left)//2
        if arr[mid] > arr[right]:
            left = mid + 1
        else:
            right = mid

    start = left
    left = 0
    right = len(arr) - 1

    if arr[start] <= target <= arr[right]:
        left = start
    else:
        right = start

    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


if __name__ == "__main__":
    nums = [45, 61, 71, 72, 73, 0, 1, 21, 33, 37]
    print(shiftedBinary(nums, 33))
