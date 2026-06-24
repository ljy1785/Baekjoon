def can_place(r, c, size, park):
    """ (r, c)를 시작점으로 size x size 크기의 돗자리를 깔 수 있는지 확인하는 함수 """
    H = len(park)
    W = len(park[0])
    
    # 돗자리가 공원 경계를 벗어나면 깔 수 없음
    if r + size > H or c + size > W:
        return False
        
    # size x size 구역 안에 사람이 있는지 검사
    for i in range(r, r + size):
        for j in range(c, c + size):
            if park[i][j] != "-1":
                return False # 사람이 있다면 실패
                
    return True # 모두 빈자리라면 성공

def solution(mats, park):
    # 1. 가장 큰 돗자리부터 찾기 위해 내림차순 정렬
    mats.sort(reverse=True)
    
    H = len(park)
    W = len(park[0])
    
    # 2. 크기가 큰 돗자리부터 차례대로 탐색
    for size in mats:
        # 공원의 모든 좌표를 돌면서 이 크기의 돗자리를 깔 수 있는지 시도
        for r in range(H):
            for c in range(W):
                if can_place(r, c, size, park):
                    return size # 큰 크기부터 돌았으므로 가능한 순간 바로 정답 반환
                    
    # 3. 모든 돗자리를 다 대입해봤는데도 깔 수 없다면 -1 반환
    return -1