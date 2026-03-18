#include <iostream>
#include <vector>
#include <string>


// Converts Decimal number to its Binary representation
// Returns String
std:: string convertDecimal( int decimal ){
    if( decimal == 0 ){
        std:: string zero = "0000";
        return zero;
    }
    std:: string binary;
    
    while( decimal != 1 ){
        if( decimal%2 == 0 ){
            binary.push_back( '0' );
        }
        else{
            binary.push_back( '1' );
        }
        decimal = decimal/2;
    }
    binary.push_back( '1' );

    int size = binary.size();
    int leadingZeros = 4 - size;
    bool firstZeros = true;
    std:: string result;

    for( int i = size - 1; i >= 0; i-- ){
        if( firstZeros ){
            for( int i = 0; i < leadingZeros; i++ ){
                result.push_back( '0' );
            }
            firstZeros = false;
        }
        result.push_back( binary[i] );
    }
    return result;
}

int main(){
    char hexDigits[] = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F'};
    int HEX_BASE = 16;

    std:: string hexaDecimal;
    std:: cin >> hexaDecimal;

    std:: vector< std:: string > binary;
    int size = hexaDecimal.size();
    
    int decimal;

    for( int i = 0; i < size; i++ ){
        for( int j = 0; j < HEX_BASE + 1; j++ ){
            if( hexDigits[j] == hexaDecimal[i] ){
                decimal = j;
                break;
            }
        }
        binary.push_back( convertDecimal( decimal) );
    }


    int binarySize = binary.size();
    for( int i = 0; i < binarySize; i++ ){
        std:: cout << binary[i];
    }
    std:: cout << "\n";
}