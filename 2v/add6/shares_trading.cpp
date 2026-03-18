#include <iostream>
#include <vector>

int main(){
    int days, initial_amount;
    std::cin >> days >> initial_amount;

    std::vector<int> asks;
    std::vector<int> bids;
    
    int ask_amount;
    for(int i = 0; i < days; i++){
        std::cin >> ask_amount;
        asks.push_back(ask_amount);
    }

    int bid_amount;
    for(int i = 0; i < days; i++){
        std::cin >> bid_amount;
        bids.push_back(bid_amount);
    }

    int current_amount;
    int max_amount = initial_amount;
    int max_shares = 0;
    int buy_day = -1;
    int sell_day = -1;
    int shares, remainder;
    int trade_occured = 0;

    for(int i = 0; i < days; i++){
        shares = initial_amount / asks[i];
        if(shares < max_shares){
            continue;
        }
        else{
            max_shares = shares;
        }
        remainder = initial_amount - shares * asks[i];
        

        for(int j = i; j < days; j++){
            current_amount = shares * bids[j];

            if(current_amount > initial_amount && current_amount > max_amount){
                max_amount = current_amount + remainder;
                buy_day = i;
                sell_day = j;
                trade_occured = 1;
            }
        }
    }

    if(trade_occured){
        std::cout << max_amount << "\n";
        std::cout << buy_day + 1 << " " << sell_day + 1 << "\n";
    }
    else{
        std::cout << initial_amount << "\n";
        std:: cout << buy_day << " " << sell_day << "\n";
    }

    return 0;
}