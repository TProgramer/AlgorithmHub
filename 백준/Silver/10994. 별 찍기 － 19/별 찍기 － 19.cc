#include <iostream>
#include <vector>
using namespace std;

int outer;
vector<vector<char>> map;

void drawCircle(int size) {

	if(size < 1) return;
	int padding = (outer - size) / 2;
	for(int i = padding; i < outer - padding; i++) {
		
		map[padding][i] = '*';
		map[outer - padding - 1][i] = '*';
		map[i][padding] = '*';
		map[i][outer - padding - 1] = '*';
	}

	drawCircle(size - 4);
}

int main() {

	int N;
	cin >> N;
	outer = (N - 1) * 4 + 1;
	map.resize(outer, vector<char>(outer, ' '));
	drawCircle(outer);
	for(auto ma : map) {
		for(auto m : ma) cout << m;
		cout << '\n';
	}
}