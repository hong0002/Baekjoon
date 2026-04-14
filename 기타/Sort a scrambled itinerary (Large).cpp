#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;

    for (int tc = 1; tc <= T; tc++) {
        int N;
        cin >> N;

        unordered_map<string, string> nextCity;
        unordered_set<string> destinations;
        vector<string> sources;

        for (int i = 0; i < N; i++) {
            string src, dst;
            cin >> src >> dst;
            nextCity[src] = dst;
            destinations.insert(dst);
            sources.push_back(src);
        }

        string start;
        for (const string &src : sources) {
            if (destinations.find(src) == destinations.end()) {
                start = src;
                break;
            }
        }

        cout << "Case #" << tc << ": ";

        string cur = start;
        for (int i = 0; i < N; i++) {
            string nxt = nextCity[cur];
            cout << cur << "-" << nxt;
            if (i != N - 1) cout << " ";
            cur = nxt;
        }
        cout << "\n";
    }

    return 0;
}
