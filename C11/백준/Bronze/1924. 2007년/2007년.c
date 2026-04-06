#include <stdio.h>

int main(){
  int x, y;
  scanf("%d %d", &x, &y);
  int month_days[] = {0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
  char* week[] = {"SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"};

  int total_days = 0;

  for (int i = 1; i < x; i++){
    total_days += month_days[i];
  }
  total_days += y;
  
  printf("%s\n", week[total_days % 7]);
  
  return 0;
}