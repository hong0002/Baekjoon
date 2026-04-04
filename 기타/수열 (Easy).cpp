#include <iostream>
#include <vector>
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

    long long answer = 0;

    for (int i = 0; i < N; i++) {
        sum = (sum - A[i] + MOD) % MOD;   // 뒤쪽 원소 합
        answer = (answer + (A[i] % MOD) * sum) % MOD;
    }

    cout << answer << '\n';
    return 0;
}
