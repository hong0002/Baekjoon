#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int z;
    cin >> z;
    while (z--) {
        int n;
        cin >> n;
        if (n % 2 == 0) cout << 'A' << "\n";
        else cout << 'B' << "\n";
    }
    return 0;
}
