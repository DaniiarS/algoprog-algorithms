#include <iostream>
#include <vector>

int is_edge(int i, int j){
    if(i==0 || j==0){
        return 1;
    }

    return 0;
}

int min(int a, int b){
    if(a < b){
        return a;
    }

    return b;
}

int main(){
    int n;
    std::cin >> n;

    std::vector<char> line(n);
    std::vector<int> prev_line(n), current_line(n);

    for(int i = 0; i < n; i++){
        std::cin >> line[i];
    }

    int max_square = 0;
    for(int i = 0; i < n; i++){
        if(line[i] == '.'){
            prev_line[i] = 0;
        }
        else{
            prev_line[i] = 1;
            max_square = 1;
        }
    }
    for(int i = 1; i < n; i++){
        // Read new line
        for(int j = 0; j < n; j++){
            std::cin >> line[j];
            current_line[j] = 0;
        }

        for(int k = 0; k < n; k++){
            if(line[k] == '#'){
                if(k==0){
                    current_line[k] = 1;
                }
                else{
                    current_line[k] = min(prev_line[k], current_line[k-1]) + 1;
                    if(current_line[k] > max_square){
                        max_square = current_line[k];
                    }
                }
            }
        }

        for(int j = 0; j < n; j++){
            prev_line[j] = current_line[j];
        }
    }
    std::cout << max_square << "\n";
}