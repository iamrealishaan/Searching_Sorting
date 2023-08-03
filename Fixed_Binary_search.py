def find_fixed_point(arr):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == mid:
            return mid
        elif arr[mid] < mid:
            right = mid - 1
        else:
            left = mid + 1

    return -1
arr = [1,2,3,4,4]
result = find_fixed_point(arr)
print(result)
