#include <bits/stdc++.h>
using namespace std;

using ll = long long;

ll gcd_ll(ll a, ll b) {
    a = llabs(a);
    b = llabs(b);
    while (b) {
        ll t = a % b;
        a = b;
        b = t;
    }
    return a;
}

// 문자열 하나를 (분자, 분모)로 변환
pair<ll, ll> parseRational(const string& s) {
    // 대분수: w,n/d
    if (s.find(',') != string::npos) {
        int commaPos = s.find(',');
        string wStr = s.substr(0, commaPos);
        string frac = s.substr(commaPos + 1);

        int slashPos = frac.find('/');
        string nStr = frac.substr(0, slashPos);
        string dStr = frac.substr(slashPos + 1);

        ll w = stoll(wStr);
        ll n = stoll(nStr);
        ll d = stoll(dStr);

        ll num = w * d + n;
        ll den = d;
        return {num, den};
    }
    // 분수: n/d
    else if (s.find('/') != string::npos) {
        int slashPos = s.find('/');
        string nStr = s.substr(0, slashPos);
        string dStr = s.substr(slashPos + 1);

        ll n = stoll(nStr);
        ll d = stoll(dStr);
        return {n, d};
    }
    // 정수: w
    else {
        ll w = stoll(s);
        return {w, 1};
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    int tc = 1;

    while (cin >> n && n != 0) {
        ll sumNum = 0;
        ll sumDen = 1;

        for (int i = 0; i < n; i++) {
            string s;
            cin >> s;

            auto [num, den] = parseRational(s);

            // sumNum/sumDen + num/den
            sumNum = sumNum * den + num * sumDen;
            sumDen = sumDen * den;

            ll g = gcd_ll(sumNum, sumDen);
            sumNum /= g;
            sumDen /= g;
        }

        // 최종 약분
        ll g = gcd_ll(sumNum, sumDen);
        sumNum /= g;
        sumDen /= g;

        ll whole = sumNum / sumDen;
        ll rem = sumNum % sumDen;

        cout << "Test " << tc++ << ": ";

        if (whole == 0 && rem == 0) {
            cout << 0;
        } else if (rem == 0) {
            cout << whole;
        } else if (whole == 0) {
            cout << rem << "/" << sumDen;
        } else {
            cout << whole << "," << rem << "/" << sumDen;
        }

        cout << "\n";
    }

    return 0;
}
