#include <stdio.h>
int num[1000001];
int main(){
  int count;
  scanf("%d", &count);
  //int num[count];
  for (int i = 0; i < count; i++){
    scanf("%d", &num[i]);
  }
  int min = num[0];
  int max = num[0];

  for (int i = 0; i<count; i++){
    if (num[i] < min){
      min = num[i];
    }
    if (num[i] > max){
      max = num[i];
    }
  }
  printf("%d %d\n", min, max);
  return 0;
}