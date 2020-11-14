#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int main() {
    int H, W, N, M;
    cin >> H >> W >> N >> M;
    int A[N], B[N], C[M], D[M];
    int g[H][W]{};
    for (int i = 0; i < N; i++) {
        cin >> A[i] >> B[i];
        A[i]--;
        B[i]--;
        g[A[i]][B[i]] = 2;
    }
    for (int i = 0; i < M; i++) {
        cin >> C[i] >> D[i];
        C[i]--;
        D[i]--;
        g[C[i]][D[i]] = -1;
    }

    for (int i = 0; i < H; i++) {
        bool is_on = false;
        bool is_on_right = false;
        for (int j = 0; j < W; j++) {
            // from left
            if (g[i][j] == 2) {
              is_on = true;
            }
            else if (g[i][j] == -1) {
              is_on = false;
            }
            else if (is_on && g[i][j]==0) {
              g[i][j] = 1;
            }

            // from right
            if (g[i][W-j-1] == 2) {
              is_on_right = true;
            }
            else if (g[i][W-j-1] == -1) {
              is_on_right = false;
            }
            else if (is_on_right && g[i][W-j-1]==0) {
              g[i][W-j-1] = 1;
            }
        }
    }

    for (int j = 0; j < W; j++) {
      bool is_on_up = false;
      bool is_on_below = false;
      for (int i = 0; i < H; i++) {
          // from up
          if (g[i][j] == 2) {
            is_on_up = true;
          }
          else if (g[i][j] == -1) {
            is_on_up = false;
          }
          else if (is_on_up && g[i][j] == 0) {
            g[i][j] = 1;
          }

          // from below
          if (g[H-i-1][j] == 2) {
            is_on_below = true;
          }
          else if (g[H-i-1][j] == -1) {
            is_on_below = false;
          }
          else if (is_on_below && g[H-i-1][j] == 0){
            g[H-i-1][j] = 1;
          }
      }
    }

    int ans = 0;
    for (int i=0; i < H; i++) {
      for (int j=0; j < W; j++) {
        if (g[i][j] > 0) {
          ans += 1;
        }
      }
    }

    cout << ans << "\n";
    return 0;
}
