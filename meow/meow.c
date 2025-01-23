#include <stdio.h>

void meow(int meows) {
  
  if( meows <= 0 )
  {
    printf("I am a cat, leave me alone\n");
    return;
  }
  else if (meows > 10)
    meows = 10;
  for (int i = 0; i < meows; i++)
    printf("meow\n");
}

int main(void) {

  char name[33];
  int meows;

  printf("What is your name: ");
  scanf("%s", name);

  printf("hello %s\n", name);
  while (1)
  {
    printf("how many meows: ");
    scanf("%d", &meows);
    if(meows == 0)
      return 1;
    
    meow(meows);
  }
  return 0;
}
