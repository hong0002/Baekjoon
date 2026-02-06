#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long T;
    int N;
    cin >> T >> N;

    vector<long long> x(N);
    for (int i = 0; i < N; i++) cin >> x[i];

    sort(x.begin(), x.end(), [](long long a, long long b) {
        return llabs(a) < llabs(b);
    });

    long long time = 0;
    long long prev = 0;
    int cnt = 0;

    for (int i = 0; i < N; i++) {
        long long d = llabs(x[i] - prev);
        if (time + d <= T) {
            time += d;
            prev = x[i];
            cnt++;
        } else {
            break;
        }
    }

    cout << cnt << "\n";
    return 0;
}
