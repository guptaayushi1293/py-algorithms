# https://www.geeksforgeeks.org/count-ways-to-reach-the-nth-station/
# input: 4
# output: 3

def total_ways_reach_station(n):
    dp = [[0 for i in range(5)]
          for i in range(n+1)]

    dp[1][1] = 1
    dp[1][2] = 1
    dp[1][3] = 1
    dp[1][4] = 1

    for i in range(2, n+1):
        if i-1 > 0 and dp[i-1][1] > 0:
            dp[i][1] = dp[i-1][4]
        if i-2 > 0 and dp[i-2][2] > 0:
            dp[i][2] = dp[i-2][4]
        if i-3 > 0 and dp[i-3][3] > 0:
            dp[i][3] = dp[i-3][4]

        dp[i][4] = dp[i][1] + dp[i][2] + dp[i][3]
    return dp[n][4]


result = total_ways_reach_station(15)
print(result)
