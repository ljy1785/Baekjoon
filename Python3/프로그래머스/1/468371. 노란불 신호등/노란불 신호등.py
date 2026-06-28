import math

def solution(signals):
    # 1. 모든 신호등의 개별 주기(G + Y + R)를 구합니다.
    cycles = [g + y + r for g, y, r in signals]
    
    # 2. 모든 주기의 최소공배수(LCM)를 구하여 딱 필요한 만큼만 상한선을 잡습니다.
    # math.lcm(*list) 구조를 사용하면 리스트 안의 모든 수의 최소공배수를 한 번에 구합니다.
    lcm_time = math.lcm(*cycles)
    
    # 3. 1초부터 최소공배수 시간까지만 탐색합니다. (효율성 극대화)
    for t in range(1, lcm_time + 1):
        all_yellow = True
        
        for g, y, r in signals:
            cycle = g + y + r
            rem = (t - 1) % cycle
            
            if not (g <= rem < g + y):
                all_yellow = False
                break
        
        if all_yellow:
            return t
            
    # 최소공배수 주기 한 바퀴를 다 돌았는데도 안 겹쳤다면 영원히 안 겹치는 것입니다.
    return -1