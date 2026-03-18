#include <iostream>
#include <vector>

int main(){
    int n;
    std:: cin >> n;
    int result = 0;

    int power = 1;

    while( n != 0 ){
        result += n%10 * power;
        n  /= 10;
        power *= 2;
    }
    std:: cout << result << "\n";
}