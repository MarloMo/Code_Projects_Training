#include <iostream>

int main() {

    // increment by 10
    std::cout << "incerementing by 10: [" << "\n";
    for (int i = 0; i < 50; i+=10) {
        std::cout << i << "\n";
    }
    std::cout << "]" << '\n';

    // decrement by 3
    std::cout << "decrementing by 3: [" << "\n";
    for (int i = 10; i >= 0; i-=3) {
        std::cout << i << "\n";
    }
    std::cout << "]" << "\n";

    return 0;
}