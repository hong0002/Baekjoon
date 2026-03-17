#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;

    vector<vector<int>> colorPoints(N + 1);

    for (int i = 0; i < N; i++) {
        int x, y;
        cin >> x >> y;
        colorPoints[y].push_back(x);
    }

    long long answer = 0;

    for (int c = 1; c <= N; c++) {
        auto &v = colorPoints[c];
        if (v.size() <= 1) continue;

        sort(v.begin(), v.end());

        int m = v.size();

        // 첫 번째 점
        answer += (long long)(v[1] - v[0]);

        // 중간 점들
        for (int i = 1; i < m - 1; i++) {
            answer += (long long)min(v[i] - v[i - 1], v[i + 1] - v[i]);
        }

        // 마지막 점
        answer += (long long)(v[m - 1] - v[m - 2]);
    }

    cout << answer << '\n';
    return 0;
}
