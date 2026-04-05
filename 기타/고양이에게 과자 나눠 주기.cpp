#include <bits/stdc++.h>
using namespace std;

using int64 = long long;

// 최대공약수
int64 gcd_ll(int64 a, int64 b) {
    while (b) {
        int64 t = a % b;
        a = b;
        b = t;
    }
    return a;
}

// 최소공배수
int64 lcm_ll(int64 a, int64 b) {
    return a / gcd_ll(a, b) * b;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    // L = lcm(1..20)
    int64 L = 1;
    for (int i = 1; i <= 20; i++) {
        L = lcm_ll(L, i);
    }

    int T;
    cin >> T;

    while (T--) {
        int N, M;
        cin >> N >> M;

        vector<int64> S(N, 0);

        for (int j = 0; j < M; j++) {
            int V;
            cin >> V;
            int64 mul = L / V;

            for (int i = 0; i < N; i++) {
                int A;
                cin >> A;
                S[i] += 1LL * A * mul;
            }
        }

        int64 mn = S[0], mx = S[0];
        for (int i = 1; i < N; i++) {
            mn = min(mn, S[i]);
            mx = max(mx, S[i]);
        }

        int64 diff = mx - mn;
        int64 g = gcd_ll(diff, L);

        int64 p = diff / g;
        int64 q = L / g;

        if (q == 1) cout << p << '\n';
        else cout << p << '/' << q << '\n';
    }

    return 0;
}
