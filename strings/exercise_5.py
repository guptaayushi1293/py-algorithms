# https://www.geeksforgeeks.org/minimize-cost-of-flipping-or-swaps-to-make-a-binary-string-balanced/
# input: 110110
# output: 1

def minimum_cost(string):
    count_1 = 0
    count_0 = 0
    length = len(string)
    for ch in string:
        count_1 = count_1 + 1 if ch == '1' else count_1
        count_0 = count_0 + 1 if ch == '0' else count_0
    if count_1 == length or count_0 == length:
        return -1
    k = abs(count_1 - count_0)
    return k//2


result = minimum_cost("11100")
print(result)