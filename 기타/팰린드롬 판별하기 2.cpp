#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    string T;
    cin >> N >> T;

    long long answer = 0;

    for (int i = 0; i < N / 2; i++) {
        char l = T[i];
        char r = T[N - 1 - i];

        if (l != '?' && r != '?') {
            if (l != r) {
                cout << 0 << '\n';
                return 0;
            }
        } else if (l == '?' && r == '?') {
            answer += 26;
        } else {
            answer += 1;
        }
    }

    cout << answer << '\n';
    return 0;
}
