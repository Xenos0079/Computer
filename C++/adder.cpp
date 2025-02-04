#include <iostream>
using namespace std;

int add(int a, int b) {
    while (b != 0) {
        int temp = a & b;
        a = a ^ b;
        b = temp << 1;
    }
    return a;
}

int main() {
    int a, b;
    cout << "Enter the first integer X: ";
    cin >> a;
    cout << "Enter the second integer Y: ";
    cin >> b;

    cout << "X + Y = " << add(a, b) << endl;
    return 0;
}
