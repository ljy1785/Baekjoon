#include <stdio.h>
#include <string.h>

int main(){
  char word[101];
  scanf("%s", word);
  int len = strlen(word);
  for (int i = 0; i < len; i += 10){
    printf("%.10s\n", word+i);
  }
  return 0;
}