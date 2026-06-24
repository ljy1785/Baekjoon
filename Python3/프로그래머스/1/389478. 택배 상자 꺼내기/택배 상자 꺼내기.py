def get_col(X, w):
    #상자 번호 X가 몇 번째 열(col)에 있는지
    row = (X - 1) // w
    if row % 2 == 0: # 짝수 층: 왼쪽 -> 오른쪽
        return (X - 1) % w
    else:            # 홀수 층: 오른쪽 -> 왼쪽
        return w - 1 - ((X - 1) % w)

def solution(n, w, num):
    # num 상자의 열 위치
    target_col = get_col(num, w)
    
    # num 상자가 위치한 층부터 시작해서 위로
    start_row = (num - 1) // w
    
    answer = 0
    # n개의 상자가 가질 수 있는 최대 층수만큼 루프
    for r in range(start_row, n + 1):
        found = False
        for X in range(r * w + 1, (r + 1) * w + 1):
            if X > n: # 전체 상자 개수를 넘어가면 더 이상 상자가 없는 것임
                break
            if get_col(X, w) == target_col:
                answer += 1
                found = True
                break
        # 만약 해당 층에서 같은 열에 있는 상자를 못 찾았다면(X > n으로 끊겼다면) 
        # 그 위층에는 더 이상 상자가 쌓여있지 않다는 뜻이므로 종료
        if not found:
            break
            
    return answer