/*
here: https://stackoverflow.com/questions/44653808/stdsystem-exception-when-instantiating-a-singleton-object
Meyers Singleton
Use this only if it's fully c++11
Why it is thread-safe: https://stackoverflow.com/questions/1661529/is-meyers-implementation-of-the-singleton-pattern-thread-safe
*/
#include <iostream>
#include <memory>

class Singleton {
    private:
        Singleton() = default;
    
    public:
        static Singleton &getInstance() {
            static Singleton instance;
            return instance;
        }

        void oi() {
            std::cout << "oi" << std::endl;
        }
};

int main() {
    Singleton& s1 = Singleton::getInstance();
    Singleton& s2 = Singleton::getInstance();
    s1.oi();

    return 0;
}