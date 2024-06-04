#include <iostream>

int main() {

    double weight1;
    int weight2;
    int weight3;

    weight1 = 156.27;
    weight2 = weight1;
    weight3 = (int) weight1;

    std::cout << weight1 << "\n";
    std::cout << weight2 << "\n";
    std::cout << weight3 << "\n"; 
    
    return 0;
}