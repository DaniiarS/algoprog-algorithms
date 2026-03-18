#include <iostream>
#include <map>

std::map<int, int> factorize(int num){
    std::map<int, int> factors;

    if(num == 1){
        factors[1] = 1;
        return factors;
    }

    int k = 2;
    while( k <= num / k){
        if(num % k == 0){
            factors[k]++;
            num = num / k;
            continue;
        }
        k++;
    }

    if(num > 1){
        // if factor[num] does not exist, facotrs[num] initlializes factors[num] to 0, and factors[num]++ makes it {num: 1}
        factors[num]++;
    }

    return factors;
}

int min_divisor(int A){
    if(A == 1){
        return A;
    }

    int min_divisor = A;

    std::map<int, int> A_factors = factorize(A);

    int N_base = 1; 
    for(const auto& [A_base, A_exponent]: A_factors){
        N_base = N_base * A_base;
    }

    for(int i = N_base; i < A + 1; i = i + N_base){
        std::map<int, int> N_factors = factorize(i);

        bool found = true;
        for(const auto& [A_base, A_exponent] : A_factors){
            if(N_factors[A_base] * i < A_exponent ){
                found = false;
                break;
            }
        }

        if(found){
            min_divisor = i;
            return min_divisor;
        }
    }

    return min_divisor;
}

int main(){
    int A;
    std::cin >> A;
    std::cout << min_divisor(A);
}