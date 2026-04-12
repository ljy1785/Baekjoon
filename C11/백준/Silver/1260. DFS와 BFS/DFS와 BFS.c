#include <stdio.h>
int graph[1001][1001];
int visited[1001];
int n, m, v;
void dfs(int current){
  visited[current] = 1;
  printf("%d ", current);
  for (int i = 1; i<=n ; i++){
    if(graph[current][i] == 1 && !visited[i]){
      dfs(i);
    }
  }
}

void bfs(int start){
  int queue[1001];
  int front = 0, rear = 0;

  queue[rear++] = start;
  visited[start]= 1;
  while(front < rear){
    int current = queue[front++];
    printf("%d ", current);
    for(int i = 1; i<= n; i++){
      if (graph[current][i] == 1 && !visited[i]){
        visited[i] = 1;
        queue[rear++] = i;
      }
    }
  }
}

int main(void) {
  scanf("%d %d %d", &n, &m, &v);
  for (int i = 0; i<m; i++){
    int a, b;
    scanf("%d %d", &a, &b);
    graph[a][b] = graph[b][a] = 1;
  }
  dfs(v);
  printf("\n");
  for (int i = 1; i <= n; i++) visited[i] = 0;

  bfs(v);
  printf("\n");
  
  
  return 0;
}