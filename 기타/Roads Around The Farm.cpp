#include <bits/stdc++.h>
using namespace std;

using ll = long long;

unordered_map<ll, ll> memo;

ll solve(ll x, ll k) {
    if (x <= k) return 1;                 // 양쪽이 nonempty가 안 되거나 차이 K 불가
    if ((x & 1) != (k & 1)) return 1;    // 홀짝 다르면 불가능

    if (memo.count(x)) return memo[x];

    ll a = (x - k) / 2;
    ll b = (x + k) / 2;

    return memo[x] = solve(a, k) + solve(b, k);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    ll N, K;
    cin >> N >> K;

    cout << solve(N, K) << '\n';
    return 0;
}
