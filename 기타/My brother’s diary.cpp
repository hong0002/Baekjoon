#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int c;
    cin >> c;
    cin.ignore();

    while (c--) {
        string s;
        getline(cin, s);

        vector<int> freq(26, 0);

        for (char ch : s) {
            if (ch != ' ') freq[ch - 'A']++;
        }

        int maxFreq = 0;
        for (int i = 0; i < 26; i++) {
            maxFreq = max(maxFreq, freq[i]);
        }

        vector<int> candidates;
        for (int i = 0; i < 26; i++) {
            if (freq[i] == maxFreq) candidates.push_back(i);
        }

        if (candidates.size() != 1) {
            cout << "NOT POSSIBLE\n";
            continue;
        }

        int most = candidates[0];
        int d = (most - ('E' - 'A') + 26) % 26;

        string decrypted = s;
        for (char &ch : decrypted) {
            if (ch == ' ') continue;
            ch = char((ch - 'A' - d + 26) % 26 + 'A');
        }

        cout << d << ' ' << decrypted << '\n';
    }

    return 0;
}
