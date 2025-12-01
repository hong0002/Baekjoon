#include <bits/stdc++.h>
using namespace std;

struct Toy {
    long long J;   // joy
    long long P;   // price
    int idx;       // 1-based index
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    if (!(cin >> N)) return 0;

    vector<Toy> toys(N);
    for (int i = 0; i < N; ++i) {
        cin >> toys[i].J >> toys[i].P;
        toys[i].idx = i + 1;  // 1-based index
    }

    // HFM = J / P 를 내림차순 정렬
    sort(toys.begin(), toys.end(), [](const Toy &a, const Toy &b) {
        __int128 lhs = (__int128)a.J * b.P;
        __int128 rhs = (__int128)b.J * a.P;
        if (lhs != rhs) return lhs > rhs;  // HFM 더 큰 게 앞으로
        // HFM이 완전히 같다면 인덱스 작은 순 등으로 정렬해도 됨 (임의)
        return a.idx < b.idx;
    });

    long long totalPrice = toys[0].P + toys[1].P + toys[2].P;
    cout << totalPrice << "\n";
    cout << toys[0].idx << "\n";
    cout << toys[1].idx << "\n";
    cout << toys[2].idx << "\n";

    return 0;
}
