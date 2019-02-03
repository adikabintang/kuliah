/*
taken from here: https://gist.github.com/pazdera/1099562
*/
#include <iostream>
#include <string>

class Cup {
    public:
        std::string color;

        Cup() : color("") {}

        // the factory method
        static Cup* getCup(std::string color);
};

class RedCup : public Cup {
    public:
        RedCup() {
            color = "red";
        }
};

class BlueCup : public Cup {
    public:
        BlueCup() {
            color = "blue";
        }
};

Cup* Cup::getCup(std::string color) {
    if (color == "red") {
        return new RedCup();
    }
    else if (color == "blue") {
        return new BlueCup();
    }
    else {
        return 0;
    }
}

int main() {
    Cup *redCup = Cup::getCup("red");
    Cup *blueCup = Cup::getCup("blue");
    std::cout << "red: " << redCup->color << std::endl;
}