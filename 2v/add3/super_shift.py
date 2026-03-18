N = int(input())
nums = list(map(int, input().split()))
K = int(input())

current_target_index = (K + 1) % N if K > 0 else -(K % N)
next_target_index = (current_target_index + K) % N if K > 0 else -(current_target_index + K + 1) % N
temp = nums[current_target_index]

for i in range(N):

    temp, nums[next_target_index] = nums[next_target_index], temp

    current_target_index = next_target_index
    next_target_index = (current_target_index + K) % N if K > 0 else -(current_target_index + K + 1)%N

for i in range(N):
    print(nums[i], end=" ")