#include <iostream>
#include <vector>
#include <string>

int main(){

    char hexDigits[] = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F'};
    int HEX_BASE = 16;
    
    std:: string binary;
    std:: cin >> binary;
    
    std:: string result;
    std:: string quadruple;
    int decimal = 0;
    int power = 1;

    int index = binary.size();

    while( index > 0 ){
        power = 1;
        decimal = 0;
        for( int i = 4; i > 0; i-- ){
            if( index < 0 ){
                break;
            }
            if( binary[index - 1] == '1' ){
                decimal += power;
            }
            power *= 2;
            index--;
        }
        result.push_back( hexDigits[decimal] );
    }

    int resultSize = result.size();
    for( int i = resultSize - 1; i >= 0; i-- ){
        std:: cout << result[i];
    }
    std:: cout << "\n";

}