/*
learned from here: https://thispointer.com//c11-multithreading-part-7-condition-variables-explained/
*/
#include <iostream>
#include <thread>
#include <mutex>
#include <condition_variable>
#include <functional>

class Application {
private:
    std::mutex _mtx;
    std::condition_variable _condVar;
    bool _isDataLoaded;

public:
    Application() : _isDataLoaded(false) {}
    bool isDataLoaded() { return _isDataLoaded; }

    void loadData() {
        // simulate blocking loading data, let's say it takes 1.5 second
        std::this_thread::sleep_for(std::chrono::milliseconds(1500));

        std::cout << "data is loaded\n";
        
        std::lock_guard<std::mutex> guard(_mtx);
        _isDataLoaded = true;

        // notify the condition variable
        _condVar.notify_one();
    }

    void mainTask() {
        std::cout << "simulate connection handshaking\n";
        // blablabla
        std::unique_lock<std::mutex> lock(_mtx);

        // this mainTask is block waiting loadData to load the data
        // wait() blocks. if the condition in std::bind(&Application::isDataLoaded) is true,
        // it wil continue. Otherwise, it will wait again.
        _condVar.wait(lock, std::bind(&Application::isDataLoaded, this));
        std::cout << "mainTask: is seems loadData is finished\n";
        std::cout << "let's continue\n";
    }
};

int main() {
    Application app;
    std::thread thread_1(&Application::mainTask, &app);
    std::thread thread_2(&Application::loadData, &app);
    thread_2.join();
    thread_1.join();
    return 0;
}