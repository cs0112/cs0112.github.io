#include <stdio.h>

int value = 100;

void set_value(int x) {
  value = x;
}

int main() {
  set_value(5);
  printf("value: %d\n", value);  
}
