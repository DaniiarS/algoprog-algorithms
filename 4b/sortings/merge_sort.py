n = int(input())

arr = list(map(int, input().split()))

def merge(left_half, right_half):
    left_edge = len(left_half) - 1
    right_edge = len(right_half) - 1

    if left_edge == 0 and right_edge == 0:
        if left_half[0] <= right_half[0]:
            return [ left_half[0], right_half[0] ]
        else:
            return [ right_half[0], left_half[0] ]

    left_ptr = 0
    right_ptr = 0

    arr = []

    while True:
        if left_half[left_ptr] <= right_half[right_ptr]:
            arr.append(left_half[left_ptr])
            left_ptr += 1
        else:
            arr.append(right_half[right_ptr])
            right_ptr += 1
        
        if left_ptr > left_edge:
            for i in range(right_edge - right_ptr + 1):
                arr.append( right_half[right_ptr])
                right_ptr += 1
            break
        elif right_ptr > right_edge:
            for i in range(left_edge - left_ptr + 1):
                arr.append(left_half[left_ptr])
                left_ptr += 1
            break
    
    return arr



def sort(arr, left, right):
    
    if left == right:
        return [ arr[left] ]
    elif right - left <= 1:
        return merge( [ arr[left] ], [ arr[right] ] )

    mid = left + (right - left)//2

    left_half = sort(arr, left, mid)
    right_half = sort(arr, mid + 1, right)

    arr = merge(left_half, right_half)

    return arr

nums = sort(arr, 0, len(arr) - 1)

for num in nums:
    print(num, end = " ")