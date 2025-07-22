#include <bits/stdc++.h>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;

    int bx, by;
    cin >> bx >> by;

    bool found = false;
    for(int i = 0; i < n; i++){
        int lx, ly, hx, hy;
        cin >> lx >> ly >> hx >> hy;
        // 점 (bx,by) 가 이 직사각형 안에 있는지 검사
        if (lx <= bx && bx <= hx && ly <= by && by <= hy) {
            found = true;
            break;  // 하나라도 만족하면 더 볼 필요 없음
        }
    }

    cout << (found ? "Yes" : "No") << "\n";
    return 0;
}
