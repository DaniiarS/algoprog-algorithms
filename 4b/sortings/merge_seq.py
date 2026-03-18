def square(x):
    return x**2

def cube(x):
    return x**3

x = int(input())
c_value = 0

square_ptr = 0
cube_ptr = 0
count = 0

square_value = 0
cube_value = 0

while(count <= x):
    square_value = square(square_ptr)
    cube_value = cube(cube_ptr)

    if(square_value < cube_value):
        square_ptr += 1
    elif(cube_value < square_value):
        cube_ptr += 1
    else:
        square_ptr += 1
        cube_ptr += 1
    count += 1

if(square_value < cube_value):
    print(square_value)
else:
    print(cube_value)
