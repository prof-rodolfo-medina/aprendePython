def diff_from_mean(arr):
    mean = sum(arr) / len(arr)
    return [abs(x - mean) for x in arr]

print(diff_from_mean([1, 2, 3, 4, 5]))  # Output: [2.0, 1.0, 0.0, 1.0, 2.0]
print(diff_from_mean([10, 20, 30, 40, 50]))  # Output: [20.0, 10.0, 0.0, 10.0, 20.0]