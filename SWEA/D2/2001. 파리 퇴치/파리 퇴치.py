T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())

    # N * N 리스트 생성, 안에 요소 넣기
    matrix = [list(map(int, input().split())) for _ in range(N)]
    # 누적합 리스트
    prefix_sum = [[0] * (N + 1) for _ in range(N + 1)]
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            prefix_sum[i][j] = matrix[i - 1][j - 1] + prefix_sum[i - 1][j] + prefix_sum[i][j - 1] - prefix_sum[i - 1][
                j - 1]

    max_value = 0
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            sum_area_val = prefix_sum[i + M][j + M] - prefix_sum[i][j + M] - prefix_sum[i + M][j] + prefix_sum[i][j]

            if max_value < sum_area_val:
                max_value = sum_area_val

    print("#{} {}".format(test_case, max_value))
