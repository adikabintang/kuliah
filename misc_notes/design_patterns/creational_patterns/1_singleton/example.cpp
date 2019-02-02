/*
taken from here: https://cppisland.com/?p=501
compile with -pthread
*/
#include <iostream>
#include <mutex>
#include <memory>

class Singleton {
    private:
        Singleton(const Singleton&) = delete;
        Singleton& operator=(const Singleton&) = delete;
        static std::unique_ptr<Singleton> instance;
        static std::once_flag onceFlag;
        Singleton() = default;
    
    public:
        static Singleton &getInstance() {
            std::call_once(Singleton::onceFlag, [](){
                instance.reset(new Singleton);
            });

            return *(instance.get());
        }

        void oi() {
            std::cout << "oi" << std::endl;
        }
};

std::unique_ptr<Singleton> Singleton::instance;
std::once_flag Singleton::onceFlag;

int main() {
    Singleton& s1 = Singleton::getInstance();
    Singleton& s2 = Singleton::getInstance();
    s1.oi();

    return 0;
}