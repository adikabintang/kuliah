/*
learn from here: https://solarianprogrammer.com/2011/12/16/cpp-11-thread-tutorial/
*/
#include <iostream>
#include <thread>

void oneFunc() {
    for (int i = 0; i < 10; i++) {
        std::cerr << "thread function executing\n";
    }
}

void threadCallback(int x, std::string s) {
    std::cout << "x: " << x << std::endl;
    std::cout << "s: " << s << std::endl;
}

void functionAskReference(int &x) {
    x++;
}

void a(int *x) {
    (*x)++;
}

int main() {
    std::thread oneThread(oneFunc);
    std::thread anotherThread([](){
        for (int i = 0; i < 10; i++) {
            std::cout << "oi another thread!\n";
        }
    });

    std::thread threadWithArg(threadCallback, 10, "Mark Tremonti");
    int n = 5;
    std::thread threadWithRef(functionAskReference, std::ref(n));
    int y = 2;
    std::thread at(a, &y);
    for (int i = 0; i < 10; i++) {
        std::cout << "display from main function\n";
    }
    
    anotherThread.join();
    oneThread.join();
    threadWithArg.join();
    threadWithRef.join();
    at.join();
    std::cout << "main: now n is " << n << std::endl;
    std::cout << "main: now y is " << y << std::endl;
    std::cout << "exit of main function\n";
    
    return 0;
}