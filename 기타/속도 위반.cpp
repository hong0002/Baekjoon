#include <bits/stdc++.h>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, M;
    cin >> N >> M;

    vector<pair<int,int>> limit(N), speed(M);
    for(int i = 0; i < N; i++){
        cin >> limit[i].first   // 구간 길이
            >> limit[i].second; // 제한속도
    }
    for(int j = 0; j < M; j++){
        cin >> speed[j].first   // 구간 길이
            >> speed[j].second; // 주행속도
    }

    int i = 0, j = 0;
    int remL = limit[0].first;
    int remS = speed[0].first;
    int ans = 0;

    while(i < N && j < M){
        // 두 구간 겹치는 길이
        int d = min(remL, remS);

        // 위반량 계산
        int diff = speed[j].second - limit[i].second;
        ans = max(ans, diff);

        // 겹친 만큼 길이 소진
        remL -= d;
        remS -= d;

        // 구간이 끝나면 다음 구간으로 이동
        if(remL == 0){
            i++;
            if(i < N) remL = limit[i].first;
        }
        if(remS == 0){
            j++;
            if(j < M) remS = speed[j].first;
        }
    }

    // 위반이 하나도 없으면 0
    cout << max(ans, 0) << "\n";
    return 0;
}
