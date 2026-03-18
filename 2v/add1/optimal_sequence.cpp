#include <iostream>
#include <vector>

int pow_10(int exp){
    int base = 1;
    int pow = 10;
    for(int i = 0; i < exp; i++){
        base = base * pow;
    }

    return base;
}

int converter(int i, int j){
    int num = j;
    int exp = 0;

    while(num != 0){
        num = num / 10;
        exp++;
    }

    return i*(pow_10(exp)) + j;
}

bool is_prime(int N){
    int k = 2;

    while(k < N/k + 1){
        if(N % k == 0){
            return false;
        }
        k++;
    }

    return true;
}

int max(int a, int b){
    if(a > b){
        return a;
    }

    return b;
}

int optimal_sequence(int N){
    std::vector<std::vector<int>> dp(N, std::vector<int>(N, 0));

    for(int i = 0; i < N; i++){
        for(int j = 0; j < N; j++){
            if(is_prime( converter(i + 1, j + 1) )){
                if(i == 0){
                    dp[i][j] = dp[i][j - 1] + 1;
                }
                else if(j == 0){
                    dp[i][j] = dp[i - 1][j] + 1;
                }
                else{
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j]) + 1;
                }
            }
            else{
                if(i == 0){
                    dp[i][j] = dp[i][j - 1];
                }
                else if(j == 0){
                    dp[i][j] = dp[i - 1][j];
                }
                else{
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j]);
                }
            }
        }
    }

    return dp[N-1][N-1] - 1;
}

int main(){
    int N;
    std::cin >> N;
    std::cout << optimal_sequence(N);
}