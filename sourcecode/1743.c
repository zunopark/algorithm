#include <stdio.h>

#define MAX 101

int N,M,K;
int matrix[MAX][MAX];
int visited[MAX][MAX];

int dx[] = {1,-1,0,0};
int dy[] = {0,0,1,-1};

int answer = 1;
int check = 0;

void init(){
    for(int i=0; i<MAX; i++){
        for(int j=0; j<MAX; j++){
            matrix[i][j] = 0;
            visited[i][j] = 0;
        }
    }
}

void dfs(int x, int y){
    visited[x][y] = 1;

    for(int i=0; i<4; i++){
        int nx = x + dx[i];
        int ny = y + dy[i];

        if (0<=nx && nx<N && 0<=ny && ny<M){
            if (matrix[nx][ny] == 1 && visited[nx][ny] == 0){
                visited[nx][ny] = 1;
                answer += 1;
                dfs(nx, ny);
            }
        }
    }

}

int main(void){
    scanf("%d %d %d", &N, &M, &K);
    init();


    for(int i=0; i<K; i++){
        int a;
        int b;
        scanf("%d %d", &a, &b);
        matrix[a-1][b-1] = 1;
    }

    // for(int i=0; i<N; i++){
    //     for(int j=0; j<M; j++){
    //         printf("%d ", matrix[i][j]);
    //     }
    //     printf("\n");
    // }

    for(int i=0; i<N; i++){
        for(int j=0; j<M; j++){
            if(matrix[i][j] == 1 && visited[i][j]==0){
                dfs(i,j);
                if(answer>check){
                    check = answer;
                }
                answer = 1;
            }
        }
    }

    // for(int i=0; i<N; i++){
    //     for(int j=0; j<M; j++){
    //         printf("%d ", matrix[i][j]);
    //     }
    //     printf("\n");
    // }

    printf("%d", check);

    return 0;
}