# 새로운 점수가 랭킹에서 몇등인지?
# 점수는 비 오름차순으로 주어진다.
import sys

number_of_rankers, my_score, ranking_length = map(int, sys.stdin.readline().split())
ranker_score_list = list(map(int, sys.stdin.readline().split()))

if number_of_rankers == 0:
    print(1)

else:
    # 1. 현재 랭킹에서 가장 낮은 점수인 것과 같은 점수
    # 2. 현재 랭킹판에 들어갈 수 있는 인원이 꽉 찬 경우
    if ranker_score_list[-1] == my_score and number_of_rankers == ranking_length:
        print(-1)
    else:
        answer = number_of_rankers + 1
        for i in range(number_of_rankers):
            if my_score >= ranker_score_list[i]:
                answer = i + 1
                break
        if answer > ranking_length:
            print(-1)
        else:
            print(answer)
