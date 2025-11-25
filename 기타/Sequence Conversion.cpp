#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    if (!(cin >> N)) return 0;

    vector<long long> a(N), b(N);
    for (int i = 0; i < N; ++i) cin >> a[i];
    for (int i = 0; i < N; ++i) cin >> b[i];

    vector<long long> d(N);
    long long tot = 0;
    for (int i = 0; i < N; ++i) {
        d[i] = a[i] ^ b[i];
        tot ^= d[i];
    }

    // 불가능한 경우
    if (tot != 0) {
        cout << -1 << '\n';
        return 0;
    }

    long long pref = 0;
    long long ans = 0;

    // x_i = d[0] ^ ... ^ d[i]  (i = 0..N-1)
    // 우리는 i = 0..N-2 (1..N-1번째 위치)에 대해 x_i != 0인 개수만 세면 됨
    for (int i = 0; i < N - 1; ++i) {
        pref ^= d[i];
        if (pref != 0) ans++;
    }

    cout << ans << '\n';
    return 0;
}
