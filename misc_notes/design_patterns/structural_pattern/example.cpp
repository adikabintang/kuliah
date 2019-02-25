/*
https://sourcemaking.com/design_patterns/adapter/cpp/1
Discussion:
LegacyRectangle's interface is not compatible with the system. 
An absctract base class is created that specifies the desired interface.
*/
#include <iostream>

typedef int Coordinate;
typedef int Dimension;

// Desired interface
class Rectangle {
    public:
        virtual void draw() = 0;
};

// Legacy component
class LegacyRectangle {
    private:
        Coordinate x1_;
        Coordinate y1_;
        Coordinate x2_;
        Coordinate y2_;
    
    public:
        LegacyRectangle(Coordinate x1, Coordinate y1, 
            Coordinate x2, Coordinate y2)
        {
            x1_ = x1;
            y1_ = y1;
            x2_ = x2;
            y2_ = y1;
            std::cout << "LegacyRectangle: create. (" << x1_
                << ", " << y1_ << ") => (" << x2_ << ", "
                << y2_ << ")" << std::endl;
        }

        void oldDraw() {
            std::cout << "LegacyRectangle: oldDraw. Drawing..." 
                << std::endl;
        }
};

// Adapter wrapper 
class RectangleAdapter: public Rectangle, private LegacyRectangle {
    public:
        RectangleAdapter(Coordinate x, Coordinate y, Dimension w, 
            Dimension h): LegacyRectangle(x, y, x+w, y+h)
        {
            std::cout << "RectangleAdapter: create. " << x 
                << "," << y << "), width = " << w 
                << ", height = " << h << std::endl;
        }

        virtual void draw() {
            std::cout << "RectangularAdapter: draw" << std::endl;
            oldDraw();
        }
};

// Now I am trying to avoid multiple inheritance...
class RectangleAdapterV2: public Rectangle {
    private:
        LegacyRectangle legacyRectangle;
    public:
        RectangleAdapterV2(Coordinate x, Coordinate y, Dimension w, 
            Dimension h): legacyRectangle(x, y, x+w, y+h)
        {
            std::cout << "RectangleAdapterV2: create. " << x 
                << "," << y << "), width = " << w 
                << ", height = " << h << std::endl;
        }

        virtual void draw() {
            std::cout << "RectangularAdapterV2: draw" << std::endl;
            legacyRectangle.oldDraw();
        }
};

int main() {
    Rectangle *r = new RectangleAdapter(120, 200, 60, 40);
    r->draw();
    Rectangle *anotherRec = new RectangleAdapterV2(120, 200, 60, 40);
    anotherRec->draw();
    return 0;
}