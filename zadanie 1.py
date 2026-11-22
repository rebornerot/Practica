# Program to find the sum of negative elements
# between the minimum and maximum elements of an array

def sum_negative_between_min_max(arr):
    min_index = arr.index(min(arr))
    max_index = arr.index(max(arr))

    start = min(min_index, max_index) + 1
    end = max(min_index, max_index)

    result = sum(x for x in arr[start:end] if x < 0)
    return result


# Example array
A = [3, -5, 7, -2, 9, -8, 4, -1]

print("Array:", A)
print("Sum of negative elements between min and max:",
      sum_negative_between_min_max(A))
