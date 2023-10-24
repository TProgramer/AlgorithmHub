#include <string>
#include <vector>
#include <iostream>
using namespace std;

string solution(int n, int t, int m, int p) {
    string answer = "";
    
    int count = 0, num = 0, idx = 0;
    while(true) {
        
        if(count >= t) break;
        string target = "";
        if (num == 0) target = "0";
        for(int i = num++; i > 0;) {
            
            int now = i % n;
            string temp = "";
            if(now > 9) temp += (char)('A' + now - 10);
            else temp = to_string(now);
            target = temp + target;
            i /= n;
        }
        for(auto ch : target) {
            
            if(++idx % m == p % m) {
                
                if(count >= t) break;
                answer += ch;
                count++;
            }
        }
    }
    return answer;
}