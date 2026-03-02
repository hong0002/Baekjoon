#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;
    vector<long long> a(N);
    for (int i = 0; i < N; i++) cin >> a[i];

    sort(a.begin(), a.end());

    int pages = 0;
    int i = 0;
    while (i < N) {
        long long m = a[i];
        long long limit = 2LL * m; // strict: price < 2*m
        int j = i;
        while (j < N && a[j] < limit) j++;
        pages++;
        i = j;
    }

    cout << pages << "\n";
    return 0;
}
