#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long N, K, P, W;
    if (!(cin >> N >> K >> P >> W)) return 0;

    long long ans = (P + W - 1) / W;  // ceil(P / W)
    cout << ans << "\n";
    return 0;
}
