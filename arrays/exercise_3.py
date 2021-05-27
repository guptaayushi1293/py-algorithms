# https://www.geeksforgeeks.org/count-number-of-common-elements-between-a-sorted-array-and-a-reverse-sorted-array/
# A = [2, 4, 5, 8, 12, 13, 17, 18, 20, 22, 309, 999]
# B = [109, 99, 68, 54, 22, 19, 17, 13, 11, 5, 3, 1]
# output = 4 (5, 13, 17, 22)


def get_common_elements(a, b, length):
    left = 0
    right = length - 1
    total_common = 0
    while left < length and right > -1:
        if a[left] == b[right]:
            total_common += 1
            left += 1
            right -= 1
        elif a[left] < b[right]:
            left += 1
        else:
            right -= 1
    return total_common


A = [2, 4, 5, 8, 12, 13, 17, 18, 20, 22, 309, 999]
B = [109, 99, 68, 54, 22, 19, 17, 13, 11, 5, 3, 1]
result = get_common_elements(A, B, len(A))
print(result)
