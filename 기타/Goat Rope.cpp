#include <iostream>
#include <cmath>
using namespace std;

int main() {
    int x, y, x1, y1, x2, y2;
    cin >> x >> y >> x1 >> y1 >> x2 >> y2;

    double dx = 0, dy = 0;

    if (x < x1) dx = x1 - x;
    else if (x > x2) dx = x - x2;

    if (y < y1) dy = y1 - y;
    else if (y > y2) dy = y - y2;

    double ans = sqrt(dx * dx + dy * dy);

    cout << ans << '\n';
    return 0;
}
