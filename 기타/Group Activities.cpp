#include <bits/stdc++.h>
using namespace std;

using int64 = long long;
using i128 = __int128_t;

int64 gcd_ll(int64 a, int64 b) {
    while (b) {
        int64 r = a % b;
        a = b;
        b = r;
    }
    return a;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;

    int64 ans;
    cin >> ans;

    for (int i = 1; i < n; i++) {
        int64 x;
        cin >> x;
        int64 g = gcd_ll(ans, x);
        ans = (i128)(ans / g) * x;
    }

    cout << ans << '\n';
    return 0;
}
