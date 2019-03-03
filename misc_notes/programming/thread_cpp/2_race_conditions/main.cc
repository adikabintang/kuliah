/*
learned from here: https://thispointer.com//c11-multithreading-part-5-using-mutex-to-fix-race-conditions/
*/
#include <iostream>
#include <mutex>
#include <vector>
#include <thread>

class Wallet {
private:
    int _money;
    std::mutex mtx;
public:
    Wallet() : _money(0) {}
    int getMoney() { return _money; }

    void addMoney(int money) {
        // with lock_guard, it will unlock when leaving this function
        // remember RAII concept
        std::lock_guard<std::mutex> lockGuard(mtx);

        for (int i = 0; i < money; i++) {
            _money++;
        }
    }
};

int main() {
    Wallet wallet;
    std::vector<std::thread> threads;
    for (int i = 0; i < 50; i++) {
        threads.push_back(std::thread(&Wallet::addMoney, &wallet, 1000));
    }

    for (int i = 0; i < threads.size(); i++) {
        threads.at(i).join();
    }
    std::cout << "money: " << wallet.getMoney() << std::endl;
    return 0;
}