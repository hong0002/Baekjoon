#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;

    vector<long long> s(N + 1), prefix(N + 1, 0);
    for (int i = 1; i <= N; i++) {
        cin >> s[i];
        prefix[i] = prefix[i - 1] + s[i];
    }

    long long ans = LLONG_MIN;

    for (int m = 1; m <= N; m++) {
        long long total = s[m] - prefix[m - 1];
        ans = max(ans, total);
    }

    cout << ans << '\n';
    return 0;
}
