#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;
    long double x1, y1, xN, yN;
    for (int i = 1; i <= N; i++) {
        long double x, y;
        cin >> x >> y;
        if (i == 1) { x1 = x; y1 = y; }
        if (i == N) { xN = x; yN = y; }
    }

    long double dx = x1 - xN;
    long double dy = y1 - yN;
    long double ans = sqrt(dx*dx + dy*dy);

    cout.setf(std::ios::fixed);
    cout << setprecision(10) << (double)ans << "\n";
    return 0;
}
