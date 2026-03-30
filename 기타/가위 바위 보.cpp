#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;

    while (T--) {
        int N;
        cin >> N;

        vector<string> robots(N);
        for (int i = 0; i < N; i++) cin >> robots[i];

        int k = robots[0].size();
        vector<bool> alive(N, true);

        auto countAlive = [&]() {
            int cnt = 0;
            for (bool x : alive) if (x) cnt++;
            return cnt;
        };

        auto winnerIndex = [&]() {
            for (int i = 0; i < N; i++) {
                if (alive[i]) return i + 1; // 1-based
            }
            return 0;
        };

        for (int round = 0; round < k; round++) {
            bool hasR = false, hasP = false, hasS = false;

            for (int i = 0; i < N; i++) {
                if (!alive[i]) continue;
                char c = robots[i][round];
                if (c == 'R') hasR = true;
                else if (c == 'P') hasP = true;
                else if (c == 'S') hasS = true;
            }

            int types = (hasR ? 1 : 0) + (hasP ? 1 : 0) + (hasS ? 1 : 0);

            // 한 종류만 있거나 세 종류 모두 있으면 탈락자 없음
            if (types == 1 || types == 3) {
                if (countAlive() == 1) break;
                continue;
            }

            char loser;
            if (hasR && hasS) loser = 'S'; // R beats S
            else if (hasS && hasP) loser = 'P'; // S beats P
            else loser = 'R'; // P beats R

            for (int i = 0; i < N; i++) {
                if (alive[i] && robots[i][round] == loser) {
                    alive[i] = false;
                }
            }

            if (countAlive() == 1) break;
        }

        if (countAlive() == 1) cout << winnerIndex() << '\n';
        else cout << 0 << '\n';
    }

    return 0;
}
