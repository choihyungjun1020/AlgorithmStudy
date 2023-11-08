# 각 단어의 길이는 3 이상 10 이하이다.
T = int(input())

for t in range(1, T+1):
    problem = list(input())
    answer = list(reversed(problem)) 
    # list.reverse() 는 원본 리스트를 뒤집는다.
    # 따라서 list(reversed(problem)) 으로 새로운 역순 리스트를 만들어준다.
    if problem == answer:
        print("#{} {}".format(t, 1))
    else:
        print("#{} {}".format(t, 0))
