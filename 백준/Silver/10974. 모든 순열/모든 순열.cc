#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {

    int N;
    bool done = false;
    cin >> N;
    vector<int> vec;
    for(int i = 1; i <= N; i++) vec.push_back(i);
    for(auto v : vec) cout << v << ' ';
    cout << '\n';
    while(!done) {

        for(int i = N - 1; i > 0; i--) {

            if(vec[i] <= vec[i - 1]) continue;

            int target = -1, min = 10000;
            for(int j = N - 1; j >= i; j--) {

                int now = vec[j] - vec[i - 1];
                if(now < min && now > 0) {
                    
                    min = now;
                    target = j;
                }
            }
            int temp = vec[target];
            vec[target] = vec[i - 1];
            vec[i - 1] = temp;
            sort(vec.begin() + i, vec.end());
            done = true;
            break;
        }
        if(!done) break;
        else for(auto v : vec) cout << v << ' ';
        cout << '\n';
        done = false;
    }
}