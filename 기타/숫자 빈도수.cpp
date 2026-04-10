#include <iostream>
using namespace std;

int main() {
    long long n, d;
    cin >> n >> d;

    long long ans = 0;

    for (long long factor = 1; factor <= n; factor *= 10) {
        long long higher = n / (factor * 10);
        long long cur = (n / factor) % 10;
        long long lower = n % factor;

        if (d != 0) {
            if (cur > d) {
                ans += (higher + 1) * factor;
            } else if (cur == d) {
                ans += higher * factor + lower + 1;
            } else {
                ans += higher * factor;
            }
        } else {
            // leading zero는 세면 안 됨
            if (higher == 0) break;

            if (cur == 0) {
                ans += (higher - 1) * factor + lower + 1;
            } else {
                ans += higher * factor;
            }
        }
    }

    cout << ans << '\n';
    return 0;
}
