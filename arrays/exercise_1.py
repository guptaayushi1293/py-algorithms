# https://www.geeksforgeeks.org/minimum-number-of-working-days-required-to-achieve-each-of-the-given-scores/
# arr[] = {400, 200, 700}
# P[] = {100, 300, 400, 500, 600}

def prefix_sum(p, length):
    for i in range(1, length):
        p[i] = p[i-1] + p[i]
    return p


def min_greater_work(prefix_p, total_work, length):
    start = 0
    end = length - 1
    last_mid = -1
    while start < end:
        mid = end - int((start + end)/2)
        if prefix_p[mid] >= total_work:
            last_mid = mid
            end = mid-1
        else:
            start = mid + 1
    return last_mid


def minimum_working_days_required(arr, p):
    length = len(p)
    prefix_p = prefix_sum(p, length)
    output = []
    for (i, number) in enumerate(arr):
        min_greater_index = min_greater_work(prefix_p, number, length)
        print("%s iteration done..." % i)
        min_days = -1 if min_greater_index == -1 else min_greater_index + 1
        output.append(min_days)
    return output


arr = [400, 200, 700]
p = [100, 300, 400, 500, 600]
result = minimum_working_days_required(arr, p)
print(result)
