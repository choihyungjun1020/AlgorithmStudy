def solution(prices):
    answer = []
    
    for i in range(len(prices)): 
        count = 0
        
        for j in range(i + 1, len(prices)):
            if(prices[i] <= prices[j]):
                count += 1
            else:
                break
                
        answer.append(count);
        
    answer.append(0); # 마지막은 변화량이 없으므로 0을 append (Java의 add)
    return answer