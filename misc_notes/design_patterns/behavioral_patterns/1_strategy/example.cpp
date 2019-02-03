/*
https://gist.github.com/Naruto/c8a1adb76cab0ec611b4
*/
#include <iostream>
#include <vector>
#include <functional>

// implementation details
class Recipes {
    public: 
        static void brewCoffee() {
            std::cout << "dripping coffee through filter\n";
        }

        static void brewTea() {
            std::cout << "steeping Tea\n";
        }

        static int amountWaterMl(int ml) {
            return ml;
        }
};

// interface defining the abstract
class CaffeineBeverage {
    private:
        void boilWater(int ml) {
            std::cout << "boiling " << ml << " ml of water\n";
        }

        void pourInCup() {
            std::cout << "pour in cup\n";
        }

        std::function<int()> _amountWaterMl;
        std::function<void()> _brew;

    public:
        CaffeineBeverage(std::function<int()> amountWaterMl, std::function<void()> brew)
            : _amountWaterMl(amountWaterMl)
            , _brew(brew) {

            }

        void prepare() {
            boilWater(_amountWaterMl());
            _brew();
            pourInCup();
        }
};

int main() {
    CaffeineBeverage coffee([](){
        return Recipes::amountWaterMl(150);
    }, &Recipes::brewCoffee);

    CaffeineBeverage tea([](){
        return Recipes::amountWaterMl(200);
    }, &Recipes::brewTea);

    CaffeineBeverage *beverage_1 = &coffee;
    CaffeineBeverage *beverage_2 = &tea;

    beverage_1->prepare();
    std::cout << "\n---------\n\n";
    beverage_2->prepare();

    return 0;    
}