def solution(board, skill):
    
    answer = 0
    
    # 스킬마다 board의 값들을 수정한다면 시간복잡도를 초과할 것으로 보임
    # 누적합을 사용해서 최종 계산을 한 번만 진행
    
    # 누적합을 계산할 보드
    accum_board = [[0] * (len(board[0]) + 1) for _ in range(len(board) + 1)]
    
    for type, r1, c1, r2, c2, degree in skill:
        # 지정된 영역에만 영향을 끼치도록 누적합 태그
        accum_board[r1][c1] += degree if type == 2 else -degree
        accum_board[r1][c2 + 1] += -degree if type == 2 else degree
        accum_board[r2 + 1][c1] += -degree if type == 2 else degree
        accum_board[r2 + 1][c2 + 1] += degree if type == 2 else -degree
    
    # 행 기준 누적합
    for i in range(len(accum_board) - 1):
        for j in range(len(accum_board[0]) - 1):
            accum_board[i][j + 1] += accum_board[i][j]
            
    # 열 기준 누적합
    for j in range(len(accum_board[0]) - 1):
        for i in range(len(accum_board) - 1):
            accum_board[i + 1][j] += accum_board[i][j]
    
    # 기존 배열과 합산하여 계산
    for i in range(len(board)):
        for j in range(len(board[i])):
            board[i][j] += accum_board[i][j]
            # board에 값이 1이상인 경우, answer 1 증가
            if board[i][j] > 0:
                answer += 1
    
    return answer