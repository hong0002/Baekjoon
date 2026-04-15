#include <iostream>
using namespace std;

int main() {
    double d, w;
    int n;
    
    cin >> d >> w >> n;
    
    double circumference = 3.14159 * d;
    double needed = w * n;
    
    if (circumference >= needed) cout << "YES\n";
    else cout << "NO\n";
    
    return 0;
}
