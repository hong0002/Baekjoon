#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;

    if (N == 2) {
        cout << "NO\n";
        return 0;
    }

    cout << "YES\n";
    if (N == 1) {
        cout << 1 << "\n";
        return 0;
    }

    // N >= 3
    cout << 1 << " " << 3 << " " << 2;
    for (int i = 4; i <= N; i++) cout << " " << i;
    cout << "\n";
    return 0;
}
