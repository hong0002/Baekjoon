#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    if (!(cin >> T)) return 0;
    while (T--) {
        int N;
        cin >> N;
        string s;
        cin >> s; // 길이 2N+1

        vector<int> a(N + 1);
        vector<char> op(N);

        for (int i = 0; i <= N; ++i) {
            a[i] = s[2 * i] - '0';
            if (i < N) op[i] = s[2 * i + 1];
        }

        int fm = -1;
        for (int i = 0; i < N; ++i) {
            if (op[i] == '-') {
                fm = i;
                break;
            }
        }

        string ans = "YES";

        if (fm == -1) {
            // 전부 +
            ans = "YES";
        } else if (fm == N - 1) {
            // 마지막 연산자만 -
            ans = "YES";
        } else {
            // fm < N-1 : 애매한 자리 a[fm+2..N]이 모두 0이어야 함
            for (int i = fm + 2; i <= N; ++i) {
                if (a[i] != 0) {
                    ans = "NO";
                    break;
                }
            }
        }

        cout << ans << '\n';
    }
    return 0;
}
