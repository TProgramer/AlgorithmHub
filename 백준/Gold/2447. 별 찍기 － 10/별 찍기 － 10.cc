#include <iostream>
#include <vector>
using namespace std;

vector<vector<char>> map;

void star(int Y, int X, int N) {

    int range = N / 3;
    for(int i = Y; i < Y + N; i += range) {
        for(int j = X; j < X + N; j += range) {

            if(i == Y + range && j == X + range) {

                for(int k = i; k < i + range; k++) {
                    for(int l = j; l < j + range; l++) map[k][l] = ' ';
                }
            }
            else if(N != 3)
                star(i, j, range);
        }
    }
}

int main() {

    int N;
    cin >> N;
    map.resize(N, vector<char>(N, '*'));
    
    star(0, 0, N);
    for(auto ma : map) {
        for(auto m : ma) cout << m;
        cout << '\n';
    }
}