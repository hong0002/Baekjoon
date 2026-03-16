#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;

    vector<long long> a(n);
    long long total_sum = 0;

    for (int i = 0; i < n; i++) {
        cin >> a[i];
        total_sum += a[i];
    }

    long long prefix_sum = 0;
    long long prefix_sq = 0;
    long long ans = 0;

    for (int i = 0; i < n - 1; i++) {
        prefix_sum += a[i];
        prefix_sq += a[i] * a[i];

        long long suffix_sum = total_sum - prefix_sum;
        ans = max(ans, prefix_sq * suffix_sum);
    }

    cout << ans << '\n';
    return 0;
}
