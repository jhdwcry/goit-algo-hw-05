def binary_search(arr, x):
    left, right = 0, len(arr) - 1
    iterations = 0
    upper_bound = None
    
    while left <= right:
        iterations += 1
        mid = left + (right - left) // 2
        if arr[mid] == x:
            return (iterations, arr[mid])
        elif arr[mid] < x:
            left = mid + 1
        else:
            upper_bound = arr[mid]
            right = mid - 1
    
    return (iterations, upper_bound)


sorted_array = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
target = 0.35
result = binary_search(sorted_array, target)
print(result)  