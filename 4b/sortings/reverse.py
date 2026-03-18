nums = [1, 2, 3, 4, 5, 6]

chars = ['a', 'b', 'c']

print(nums[::-1])
print(chars[::-1])

size = len(nums)


# Проходимся с конца в начало
for i in range(size):
    print( nums[-1 - i] )



# nums = [1, 2, 3]
# nums = [3, 2, 1]

# Меняем значения в самом массиве
for i in range(size//2):

    nums[i], nums[-1 - i] = nums[-1-i], nums[i]

print(nums)