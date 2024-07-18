def solution(routes):
    
    answer = 0
    
    # 진출 시점을 기준으로 오름차순 정렬한 후
    # 정렬된 배열을 순회하며, 진입 시점을 직전 진출 시점과 비교
    # 작거나 같다면 같은 카메라로 단속 가능 / 크다면 새로운 카메라가 필요
    sorted_routes = sorted(routes, key = lambda val: val[1])
    
    # 직전 진출 시점을 담을 변수
    latest_exit = -30001
    
    for route in sorted_routes:
        if route[0] > latest_exit:
            answer += 1
            latest_exit = route[1]
    
    return answer