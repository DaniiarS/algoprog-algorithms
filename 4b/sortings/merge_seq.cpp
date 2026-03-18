#include <iostream>
#include <climits>
#include <cstdint>
#include <string>

unsigned long long int square(unsigned long long int x){
    return x*x;
}

unsigned long long int cube(unsigned long long int x){
    return x*x*x;
}

int main(){
    unsigned long long int x;
    std::cin >> x;

    unsigned long long int c_value = 0;
    unsigned long long int square_ptr = 0;
    unsigned long long int cube_ptr = 0;
    unsigned long long int count = 0;

    unsigned long long int square_value = 0;
    unsigned long long int cube_value = 0;

    while(count <= x){
        square_value = square(square_ptr);
        cube_value = cube(cube_ptr);

        if(square_value < cube_value){
            square_ptr++;
        }
        else if(cube_value < square_value){
            cube_ptr++;
        }
        else{
            square_ptr++;
            cube_ptr++;
        }
        count++;
    }

    if(square_value < cube_value){
        c_value = square_value;
    }
    else{
        c_value = cube_value;
    }
    std:: cout << c_value << std::endl;
}