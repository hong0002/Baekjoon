#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;
    long long ans = 1;
    for (int i = 2; i <= N; i++) ans *= i;
    cout << ans << "\n";
    return 0;
}
