# 시 / 분으로 이루어진 시각을 2개 입력받아 더한 값을 시 분으로 출력하는 프로그램
# 시 1 이상 12 이하의 정수, 분 0 이상 59 이하의 정수

T = int(input())

for t in range(1, T + 1):
    t1, m1, t2, m2 = map(int, input().split())
    answer_t = t1 + t2 + ((m1 + m2) // 60)
    answer_m = (m1 + m2) % 60
    if answer_t > 12:
        answer_t -= 12
    print(f"#{t} {answer_t} {answer_m}")
