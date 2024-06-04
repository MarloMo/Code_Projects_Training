/// Unlike regular functions, templates are entirely created in header files.

template <typename T> T get_smallest(T num1, T num2) {

  return num2 < num1 ? num2 : num1;
}
