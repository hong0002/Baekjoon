#include <bits/stdc++.h>
using namespace std;

const long long MOD = 1000000007LL;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;

    vector<long long> A(N);
    long long sum = 0;

    for (int i = 0; i < N; i++) {
        cin >> A[i];
        sum = (sum + A[i]) % MOD;
    }

    long long ans = 0;

    for (int i = 0; i < N; i++) {
        sum = (sum - A[i] + MOD) % MOD;   // 뒤에 남은 원소들의 합
        ans = (ans + A[i] * sum) % MOD;
    }

    cout << ans % MOD << '\n';
    return 0;
}
