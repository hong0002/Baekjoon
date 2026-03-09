#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, D;
    cin >> N >> D;

    long long answer = 0;
    int prev = -1;

    for (int i = 1; i <= N; i++) {
        int x;
        cin >> x;
        if (x == 1) {
            if (prev != -1) {
                int gap = i - prev;
                answer += (gap - 1) / D;
            }
            prev = i;
        }
    }

    cout << answer << '\n';
    return 0;
}
