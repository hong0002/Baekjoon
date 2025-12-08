#include <bits/stdc++.h>
using namespace std;

// n을 base 진법 문자열로 변환 (base는 2~10)
string to_base(long long n, int base) {
    if (n == 0) return "0";
    string s;
    while (n > 0) {
        int r = n % base;
        s.push_back('0' + r);  // base <= 10 이므로 숫자만 사용
        n /= base;
    }
    reverse(s.begin(), s.end());
    return s;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long H, T, C, K, G;
    cin >> H >> T >> C >> K >> G;

    int M;
    cin >> M;

    long long cnt[5] = {H, T, C, K, G};
    char name[5] = {'H', 'T', 'C', 'K', 'G'};

    long long prev_total = H + T + C + K + G;

    for (int i = 0; i < M; i++) {
        long long h, t, c, k, g;
        cin >> h >> t >> c >> k >> g;

        cnt[0] -= h;
        cnt[1] -= t;
        cnt[2] -= c;
        cnt[3] -= k;
        cnt[4] -= g;

        long long cur_total = cnt[0] + cnt[1] + cnt[2] + cnt[3] + cnt[4];

        // 진법 결정
        int d = prev_total % 10;
        int base = (d == 0 || d == 1) ? 10 : d;

        // 1줄차: 진법 변환 + "7H"
        string rep = to_base(cur_total, base);
        cout << rep << "7H\n";

        // 2줄차: 정렬 후 알파벳 출력 혹은 NULL
        if (cur_total == 0) {
            cout << "NULL\n";
        } else {
            vector<pair<long long, char>> v;
            for (int j = 0; j < 5; j++) {
                if (cnt[j] > 0) {
                    v.push_back({cnt[j], name[j]});
                }
            }
            sort(v.begin(), v.end(), [](auto &a, auto &b) {
                if (a.first != b.first) return a.first > b.first; // 개수 내림차순
                return a.second < b.second;                       // 알파벳 오름차순
            });
            for (auto &p : v) cout << p.second;
            cout << '\n';
        }

        prev_total = cur_total;
    }

    return 0;
}
