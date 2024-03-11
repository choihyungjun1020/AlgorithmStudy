# n은 동전의 가지 수
# k는 가치의 합
n, k = map(int, input().split())
coins = []

for _ in range(n):
    coins.append(int(input()))

# 메모이제이션 활용

dp = [0] * (k + 1)
dp[0] = 1  # 0을 만드는 경우의 수는 항상 1개

for coin in coins:
    for i in range(coin, k + 1):
        dp[i] += dp[i - coin]

print(dp[k])