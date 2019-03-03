/*
learned from here: https://thispointer.com//c11-multithreading-part-8-stdfuture-stdpromise-and-returning-values-from-thread/
use case: we want a thread to return a result.
*/
#include <iostream>
#include <thread>
#include <future>

void initiazer(std::promise<int> *promObj) {
    std::cout << "Inside thread\n";
    promObj->set_value(35);
}

int main() {
    std::promise<int> promiseObj;
    std::future<int> futureObj = promiseObj.get_future();
    std::thread th(initiazer, &promiseObj);
    std::cout << futureObj.get() << std::endl;
    th.join();
    return 0;
}