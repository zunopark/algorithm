#include <stdio.h>
#include <stdlib.h>
#define MAX 51


int dx[] = {1,-1,0,0};
int dy[] = {0,0,1,-1};

int matrix[MAX][MAX];
int visited[MAX][MAX];

void dfs(int x, int y, int m, int n);

void init(){
    for(int i=0; i<MAX; i++){
        for(int j=0; j<MAX; j++){
            matrix[i][j] = 0;
            visited[i][j] = 0;
        }
    }
}


void dfs(int x, int y, int m, int n){
    visited[x][y] = 1;

    for(int i=0; i<4; i++){
        int nx = x + dx[i];
        int ny = y + dy[i];

        if(0<= nx && nx<n && 0<=ny && ny<m){
            if(matrix[nx][ny] == 1 && visited[nx][ny] == 0){
                visited[nx][ny] = 1;
                dfs(nx, ny, m, n);
            }
        }

    }

}

int main(void){
    int t_case;
    scanf("%d", &t_case);

    while (t_case>0){
        init();
        int cnt = 0;
        int m,n,k;
        scanf("%d %d %d", &m, &n, &k);


        for(int i=0; i<k; i++){
            int a,b;
            scanf("%d %d", &a, &b);
            matrix[b][a] = 1;
        }

        for(int i=0; i<n; i++){
            for(int j=0; j<m; j++){
                if(matrix[i][j] == 1 && visited[i][j] == 0){
                    dfs(i,j, m, n);
                    cnt += 1;
                }
            }
        }

        printf("%d\n", cnt);

        t_case -= 1;
    }

    return 0;
}