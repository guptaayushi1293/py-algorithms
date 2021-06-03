# Check whether a title in netflix is increasing or decreasing in popularity
# input = [1, 2, 2, 3] -- increasing
# input = [8,8,7,6,5,4,4,1] -- decreasing
# input = [4,5,6,3,4] -- fluctuating

def check_popularity(arr):
    increasing = decreasing = True
    length = len(arr)
    for index in range(1, length):
        if arr[index] > arr[index - 1]:
            decreasing = False
        if arr[index] < arr[index - 1]:
            increasing = False
    return increasing or decreasing


movie_ratings = [
    [1, 2, 2, 3],
    [8, 8, 7, 6, 5, 4, 4, 1],
    [4, 5, 6, 3, 4]
]

for each_rating_week in movie_ratings:
    print(check_popularity(each_rating_week))
