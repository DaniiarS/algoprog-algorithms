#include <iostream>
#include <vector>
#include <string>


int main(){
    int n,k;
    std:: string A;

    int alphabetSize = 26;
    int digitsAmount = 10;
    
    std:: string digits;

    for( int i = 0; i < digitsAmount; i++ ){
        digits.push_back( char( '0' + i ) );
    }

    for( int i = 0; i < alphabetSize; i++ ){
        digits.push_back( char( 'A' + i ) );
    }

    std:: cin >> n >> A >> k;


    
}