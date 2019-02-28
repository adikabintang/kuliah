#include <iostream>

using namespace std;

int fibonacci(int n) {
    int prev_fib = 0;
    int current_fib = 1;
    int res = prev_fib;
    for (int i = 1; i < n; i++) {
        int temp = current_fib;
        current_fib += prev_fib;
        prev_fib = temp;
        res = current_fib;
    }

    return res;
}

int main() {
    int n;
    cin >> n;
    cout << fibonacci(n);
    return 0;
}

