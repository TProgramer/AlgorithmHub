#include <iostream>
using namespace std;

int main() {

	int	N;
	cin >> N;

	if(N == 1) {

		cout << '*';
		return 0;
	}

	int size = (N - 1) * 4 + 1;
	for(int i = 0; i < size; i++) cout << '*';
	cout << '\n' << '*' << '\n';
	int miniSize = size - 2;
	for(int i = 0; i < N - 1; i++) {

		cout << '*' << ' ';
		for(int j = 0; j < i; j++) cout << '*' << ' ';
		for(int j = 0; j < miniSize - i * 4; j++) cout << '*';
		for(int j = 0; j < i; j++) cout << ' ' << '*';
		cout << '\n' << '*' << ' ';
		for(int j = 0; j < i + 1; j++) cout << '*' << ' ';
		for(int j = 0; j < miniSize - (i + 1) * 4; j++) cout << ' ';
		for(int j = 0; j < i + 1; j++) {
			
			if(i == N - 2) {
				
				if(j == 0) cout << '*';
				if(j == i) continue;
			}
			cout << ' ' << '*';
		}
		cout << '\n';
	}

	for(int i = N - 1; i >= 0; i--) {

		for(int j = 0; j < i; j++) cout << '*' << ' ';
		for(int j = 0; j < size - i * 4; j++) cout << '*';
		for(int j = 0; j < i; j++) cout << ' ' << '*';
		cout << '\n';
		if(i == 0) continue;
		for(int j = 0; j < i; j++) cout << '*' << ' ';
		for(int j = 0; j < size - i * 4; j++) cout << ' ';
		for(int j = 0; j < i; j++) cout << ' ' << '*';
		cout << '\n';
	}
}