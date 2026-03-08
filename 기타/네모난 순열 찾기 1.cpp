#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;

    vector<vector<int>> A(N, vector<int>(N));
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            cin >> A[i][j];
        }
    }

    long long answer = 0;

    for (int r1 = 0; r1 < N; r1++) {
        for (int r2 = r1; r2 < N; r2++) {
            for (int c1 = 0; c1 < N; c1++) {
                for (int c2 = c1; c2 < N; c2++) {
                    int h = r2 - r1 + 1;
                    int w = c2 - c1 + 1;
                    int area = h * w;

                    bool seen[226] = {};  // N^2 <= 225
                    bool ok = true;

                    for (int r = r1; r <= r2 && ok; r++) {
                        for (int c = c1; c <= c2; c++) {
                            int v = A[r][c];
                            if (v > area || seen[v]) {
                                ok = false;
                                break;
                            }
                            seen[v] = true;
                        }
                    }

                    if (ok) answer++;
                }
            }
        }
    }

    cout << answer << '\n';
    return 0;
}
