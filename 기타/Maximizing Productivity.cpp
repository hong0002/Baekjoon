#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int N, Q;
    cin >> N >> Q;

    vector<int> c(N), t(N);
    for(int i = 0; i < N; i++) cin >> c[i];
    for(int i = 0; i < N; i++) cin >> t[i];

    vector<int> d(N);
    for(int i = 0; i < N; i++){
        d[i] = c[i] - t[i];
    }
    sort(d.begin(), d.end());

    while(Q--){
        int V, S;
        cin >> V >> S;
        // d_i > S 인 첫 위치
        auto it = upper_bound(d.begin(), d.end(), S);
        int cnt = d.end() - it;
        cout << (cnt >= V ? "YES\n" : "NO\n");
    }

    return 0;
}
