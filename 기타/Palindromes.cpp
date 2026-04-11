#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    map<char, char> mirror;
    mirror['A'] = 'A';
    mirror['E'] = '3';
    mirror['3'] = 'E';
    mirror['H'] = 'H';
    mirror['I'] = 'I';
    mirror['J'] = 'L';
    mirror['L'] = 'J';
    mirror['M'] = 'M';
    mirror['O'] = 'O';
    mirror['S'] = '2';
    mirror['2'] = 'S';
    mirror['T'] = 'T';
    mirror['U'] = 'U';
    mirror['V'] = 'V';
    mirror['W'] = 'W';
    mirror['X'] = 'X';
    mirror['Y'] = 'Y';
    mirror['Z'] = '5';
    mirror['5'] = 'Z';
    mirror['1'] = '1';
    mirror['8'] = '8';

    string s;
    while (cin >> s) {
        bool isPalindrome = true;
        bool isMirrored = true;
        int n = s.size();

        for (int i = 0; i < n; i++) {
            if (s[i] != s[n - 1 - i]) {
                isPalindrome = false;
            }

            if (mirror.find(s[n - 1 - i]) == mirror.end() ||
                s[i] != mirror[s[n - 1 - i]]) {
                isMirrored = false;
            }
        }

        cout << s << " -- ";
        if (isPalindrome && isMirrored) {
            cout << "is a mirrored palindrome.\n\n";
        } else if (isPalindrome) {
            cout << "is a palindrome.\n\n";
        } else if (isMirrored) {
            cout << "is a mirrored string.\n\n";
        } else {
            cout << "is not a palindrome.\n\n";
        }
    }

    return 0;
}
