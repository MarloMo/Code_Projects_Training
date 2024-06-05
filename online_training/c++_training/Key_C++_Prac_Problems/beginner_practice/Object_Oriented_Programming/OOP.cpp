#include <iostream>

class Animal {
public:
  /// In this example, speak is a virtual function. The virtual keyword
  /// indicates that this function can be overridden in any derived class.
  /// It allows you to achieve polymorphism, where a base class pointer or
  /// reference can call a derived class's method.
  virtual void speak() const {
    std::cout << "Animal sound"
              << "\n";
  }
};

class Dog : public Animal {
public:
  /// In this example, speak is overridden in the Dog class. The override
  /// keyword ensures that this function is overriding a virtual function from
  /// the base class.
  void speak() const override {
    std::cout << "Woof!"
              << "\n";
  }
};

class Cat : public Animal {
public:
  void speak() const override {
    std::cout << "Meow!"
              << "\n";
  }
};

int main() {

  Animal dog;
  dog.speak(); /// output: Animal sound

  Dog Spot;
  Spot.speak(); /// output: Woof!

  /// Polymorphism: In the main function, an Animal pointer points to a Dog
  /// object. When speak is called on myAnimal, it invokes the speak method of
  /// Dog, demonstrating polymorphism.
  Animal *myAnimal = new Dog();
  myAnimal->speak(); // Output: Woof!

  return 0;
}