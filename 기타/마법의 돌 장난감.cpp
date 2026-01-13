#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;
    vector<int> A(N + 1);
    for (int i = 1; i <= N; i++) cin >> A[i];

    vector<pair<int,int>> ops;

    for (int i = 1; i <= N; i++) {
        int pos = -1;
        for (int j = i; j <= N; j++) {
            if (A[j] == i) { pos = j; break; }
        }
        if (pos == -1) return 0; // permutation이 아니면 문제 조건 위배(발생 안 함)
        if (pos == i) continue;

        // reverse A[i..pos]
        reverse(A.begin() + i, A.begin() + pos + 1);
        ops.push_back({i, pos});
    }

    // ops.size()는 최대 N-1 <= 99
    cout << ops.size() << "\n";
    for (auto &p : ops) {
        cout << p.first << " " << p.second << "\n";
    }
    return 0;
}
