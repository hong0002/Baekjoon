#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    // 예제 2에 주어진 25개의 앨범 정보
    const vector<pair<int, string>> albums = {
        {1967, "DavidBowie"},
        {1969, "SpaceOddity"},
        {1970, "TheManWhoSoldTheWorld"},
        {1971, "HunkyDory"},
        {1972, "TheRiseAndFallOfZiggyStardustAndTheSpidersFromMars"},
        {1973, "AladdinSane"},
        {1973, "PinUps"},
        {1974, "DiamondDogs"},
        {1975, "YoungAmericans"},
        {1976, "StationToStation"},
        {1977, "Low"},
        {1977, "Heroes"},
        {1979, "Lodger"},
        {1980, "ScaryMonstersAndSuperCreeps"},
        {1983, "LetsDance"},
        {1984, "Tonight"},
        {1987, "NeverLetMeDown"},
        {1993, "BlackTieWhiteNoise"},
        {1995, "1.Outside"},
        {1997, "Earthling"},
        {1999, "Hours"},
        {2002, "Heathen"},
        {2003, "Reality"},
        {2013, "TheNextDay"},
        {2016, "BlackStar"}
    };

    int Q;
    cin >> Q;
    while (Q--) {
        int S, E;
        cin >> S >> E;

        // 해당 기간에 속하는 앨범만 골라서 출력
        vector<pair<int, string>> result;
        for (auto &alb : albums) {
            if (alb.first >= S && alb.first <= E) {
                result.push_back(alb);
            }
        }

        // 결과 출력
        cout << result.size() << '\n';
        for (auto &alb : result) {
            cout << alb.first << ' ' << alb.second << '\n';
        }
    }

    return 0;
}
