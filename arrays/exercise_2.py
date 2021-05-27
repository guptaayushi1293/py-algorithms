# https://www.geeksforgeeks.org/smallest-index-that-splits-an-array-into-two-subarrays-with-equal-product/
# arr = [1,2,3,3,2,1]
# output = 3 (index + 1)

def minimum_index_equal_product_subarray(arr, length):
    product = 1
    for (i, number) in enumerate(arr, length):
        product *= number
    left = 1
    right = product
    for (i, number) in enumerate(arr):
        left *= number
        right = int(right/number)
        if left == right:
            return i+1
    return -1


arr = [3, 2, 6]
result = minimum_index_equal_product_subarray(arr, len(arr))
print(result)
