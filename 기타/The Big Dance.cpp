#include <iostream>
using namespace std;

long long ans = 0;

void solve(int l, int r) {
    int len = r - l + 1;

    if (len == 1) {
        return;
    }

    if (len == 2) {
        ans += 1LL * l * r;
        return;
    }

    int left_size = (len + 1) / 2;
    int mid = l + left_size - 1;

    solve(l, mid);
    solve(mid + 1, r);
}

int main() {
    int N;
    cin >> N;

    solve(1, N);

    cout << ans << '\n';

    return 0;
}
