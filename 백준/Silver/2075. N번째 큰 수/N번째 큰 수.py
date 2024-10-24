import heapq

# 주어지는 N번째 큰 수를 적은 메모리로 찾기위해 제한적인 heap 에서 진행
# 전체 입력값을 배열로 받아올 시, 메모리 초과 발생
pQueue = []
n = int(input())

for _ in range(n):
    nums = map(int, input().split())
    for num in nums:
        # heap 의 크기를 n 이하로 유지
        if len(pQueue) >= n:
            if pQueue[0] < num:
                heapq.heappop(pQueue)
                heapq.heappush(pQueue, num)
        else:
            heapq.heappush(pQueue, num)
            
print(pQueue[0])