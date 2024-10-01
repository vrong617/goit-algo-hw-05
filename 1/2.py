def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    iterations = 0
    upper_bound = None

    while left <= right:
        iterations += 1
        mid = (left + right) // 2
        mid_value = arr[mid]

        if mid_value == target:
            return iterations, mid_value
        elif mid_value < target:
            left = mid + 1
        else:
            upper_bound = mid_value
            right = mid - 1

    if upper_bound is None and left < len(arr):
        upper_bound = arr[left]
    return iterations, upper_bound


sorted_array = [0.1, 0.5, 1.3, 2.8, 3.7, 4.2, 5.9]
target = 4.0
result = binary_search(sorted_array, target)

print(f"Кількість ітерацій: {result[0]}")
print(f"Верхня межа для {target}: {result[1]}")
