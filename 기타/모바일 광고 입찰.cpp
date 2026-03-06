#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, K;
    cin >> N >> K;

    vector<long long> need(N);

    for (int i = 0; i < N; i++) {
        long long A, B;
        cin >> A >> B;
        need[i] = max(0LL, B - A);
    }

    sort(need.begin(), need.end());

    cout << need[K - 1] << '\n';
    return 0;
}
