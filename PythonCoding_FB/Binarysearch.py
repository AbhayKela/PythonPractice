def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1 #returns -1 if target is not found

arr = [2,3,5,7,8]
target = 5
result = binary_search(arr, target)
if result != -1:
    print(f"Element {target} found at index {result}")
else:
    print("Element not found")