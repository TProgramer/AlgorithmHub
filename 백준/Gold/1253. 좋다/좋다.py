# 입력값들을 정렬시키고 왼쪽과 오른쪽 끝에 투포인터를 좁혀가며,
# 좋다에 해당하는 수 찾기
n = int(input())
arr = list(map(int, input().split()))
arr.sort()
answer = 0

for i in range(n):
    # 순차적으로 숫자 하나씩 검사
    target = arr[i]
    left = 0
    right = len(arr) - 1
    while left < right:
        if arr[left] + arr[right] > target:
            right -= 1
        elif arr[left] + arr[right] < target:
            left += 1
        else:
            if left == i:
                left += 1
            elif right == i:
                right -= 1
            else:
                answer += 1
                break
            
print(answer)