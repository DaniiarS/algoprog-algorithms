#include <iostream>
#include <vector>
#include <string>

int main(){
    int number;
    std:: cin >> number;

    std:: string binary;
    
    while( number != 1 ){
        if( number%2 == 0 ){
            binary.push_back( '0' );
        }
        else{
            binary.push_back( '1' );
        }
        number = number/2;
    }
    binary.push_back(number);

    std:: cout << "\n";
}