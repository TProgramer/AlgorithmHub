#include <iostream>
#include <string>
using namespace std;

void vps(int n, int k) {

    int arr[n];

    for(int i=1; i<=n; i++) { arr[i-1] = i; }

    int total = n;
    int count = k;
    cout << "<";

    for(int i=0; ; i = (++i) % n) {

        if(count != 1 && arr[i] != -1) count--;

        else if(total == 1 && arr[i] != -1) {
            
            cout << arr[i] << ">";
            arr[i] = -1;
            total--;
        }

        else if(count == 1 && arr[i] != -1) {

            cout << arr[i] << ", ";
            arr[i] = -1;
            total--;
            count = k;
        }

        if(total == 0) break;
    }
}

int main() {
    
    cin.tie(NULL);
    ios_base::sync_with_stdio(false);
    
    int N, K;

    cin >> N >> K;

    vps(N, K);    

    return 0;
}