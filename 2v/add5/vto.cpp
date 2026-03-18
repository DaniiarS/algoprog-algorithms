#include <iostream>

std::pair<double, double> line(std::pair<int, int> p1, std::pair<int, int> p2){
    int x1 = p1.first;
    int y1 = p1.second;

    int x2 = p2.first;
    int y2 = p2.second;

    double k = double(y1 - y2)/(x1 - x2);
    double m = y1 - k * x1;

    return {k, m};
}

int count_squares(int a, int b, int N){
    int origin = 0;
    std::pair<double, double> coef = line( {origin, a}, {b, origin} );

    int count = 0;
    for(int x = 1; x <= b; x++){
        count = count + int(coef.first * x + coef.second);
    }

    return N - count % N;
}

int main(){
    int a, b, N;
    std::cin >> a >> b >> N;
    std::cout << count_squares(a, b, N);
}