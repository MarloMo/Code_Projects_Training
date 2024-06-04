### REVIEW

* Scope is the region of code that has access to an element.
    * Globally scoped variables are accessible everywhere.
    * A variable created inside a function has local scope and can’t be accessed outside the function.

* C++ functions are usually split to make code more modular:
    * The declaration in a header file.
    * The definition in another .cpp file.

* Programs with multiple .cpp files need to be linked at compile time:

```
g++ main.cpp fns.cpp
```

