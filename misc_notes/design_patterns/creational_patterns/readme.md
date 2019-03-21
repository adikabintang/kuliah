## Singleton

```cpp
class MyClass {
private:
    MyClass() {} // private constructor
    static std::unique_ptr<MyClass> instance; // the single instance we're gonna return
    static std::once_flag onceFlag; // the once-only flag to avoid race condition
public:
    static std::unique_ptr<MyClass> &getInstance() {
        std::call_once(onceFlag, []() {
		instance.reset(new MyClass());
	});

        return instance;
    }

    void foo() {
        std::cout << "hello world\n";
    }
};
```

and in another class/function, when you need the object from this class, just call:

```cpp
int main() {
    auto &myObject = MyClass::getInstance();
    myObject->foo();
}
```

## Factory
### 1. Create the interface/base class

```cpp
class Car {
public:
    virtual void setColor(const char *color) = 0;
    virtual ~Car() {} // destructor is needed to avoid undefined behavior
};
```

### 2. Create the derived class

```cpp
class Toyota : public Car {
    std::string color = "";
public: 
    void setColor(const char *color) {
        this->color = color;
    }
    
    ~Toyota() {}
};
```

and another one or more:
```cpp
class Isuzu : public Car {
    std::string color = "";
public: 
    void setColor(const char *color) {
        this->color = color;
    }
    
    ~Isuzu() {}
};
```

### 3. Create the factory class
```cpp
class CarFactory {
    static std::unique_ptr<Car> getCarByBrand(const char *brandName) {
        if (strcmp(brandName, "Toyota") == 0) { // Do not use == for const char * comparison. std::string may use ==
            return std::make_unique<Toyota>();
        }
        else if (strcmp(brandName, "Isuzu") == 0) {
            return std::make_unique<Isuzu>();
        }
        
        throw std::exception("We do not have that car yet");
    }
};
```

### 4. Let's use it

```cpp
int main() {
    try {
        std::unique_ptr<Car> myCar = CarFactory::getCarByBrand("Toyota"); // or use 'auto' instead
    }
    catch (std::exception &e) {
        std::cout << "error getting new class: " << e.what() << std::endl;
    }
}
```