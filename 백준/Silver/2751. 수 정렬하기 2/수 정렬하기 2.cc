#include <iostream>
#include <set>
using namespace std;

int main() {

	int N;
	cin >> N;
	set<int> list;

	int temp;
	while(N--) {

		cin >> temp;
		list.insert(temp);
	}

	for(auto li : list) cout << li << '\n';
}