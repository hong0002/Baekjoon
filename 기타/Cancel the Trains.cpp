#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;

    while (t--) {
        int n, m;
        cin >> n >> m;

        bool bottom[101] = {false};

        for (int i = 0; i < n; i++) {
            int x;
            cin >> x;
            bottom[x] = true;
        }

        int answer = 0;
        for (int i = 0; i < m; i++) {
            int x;
            cin >> x;
            if (bottom[x]) answer++;
        }

        cout << answer << '\n';
    }

    return 0;
}
