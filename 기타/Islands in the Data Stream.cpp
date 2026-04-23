#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int P;
    cin >> P;

    while (P--) {
        int K;
        cin >> K;

        vector<int> a(15);
        int maxH = 0;
        for (int i = 0; i < 15; i++) {
            cin >> a[i];
            maxH = max(maxH, a[i]);
        }

        int islands = 0;

        for (int h = 1; h <= maxH; h++) {
            bool inIsland = false;
            for (int i = 0; i < 15; i++) {
                if (a[i] >= h) {
                    if (!inIsland) {
                        islands++;
                        inIsland = true;
                    }
                } else {
                    inIsland = false;
                }
            }
        }

        cout << K << ' ' << islands << '\n';
    }

    return 0;
}
