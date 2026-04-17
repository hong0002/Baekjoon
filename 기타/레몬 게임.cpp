#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;

    long long cnt1 = 0, cnt2 = 0;
    for (int i = 0; i < N; i++) {
        int x;
        cin >> x;
        if (x == 1) cnt1++;
        else cnt2++;
    }

    if (cnt1 >= cnt2 && (cnt1 + 2 * cnt2) % 3 == 0) {
        cout << "Yes\n";
    } else {
        cout << "No\n";
    }

    return 0;
}
