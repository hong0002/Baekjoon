#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    cin >> n >> m;

    vector<long long> A(n);
    for (int i = 0; i < n; i++) {
        cin >> A[i];
    }

    sort(A.begin(), A.end());

    while (m--) {
        int type;
        cin >> type;

        if (type == 1) {
            long long k;
            cin >> k;
            auto it = lower_bound(A.begin(), A.end(), k);
            cout << (A.end() - it) << '\n';
        }
        else if (type == 2) {
            long long k;
            cin >> k;
            auto it = upper_bound(A.begin(), A.end(), k);
            cout << (A.end() - it) << '\n';
        }
        else if (type == 3) {
            long long i, j;
            cin >> i >> j;
            auto l = lower_bound(A.begin(), A.end(), i);
            auto r = upper_bound(A.begin(), A.end(), j);
            cout << (r - l) << '\n';
        }
    }

    return 0;
}
