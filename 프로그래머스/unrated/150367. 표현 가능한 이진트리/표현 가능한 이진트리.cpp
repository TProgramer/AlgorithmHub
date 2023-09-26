#include <string>
#include <vector>

using namespace std;

bool search(string str) {
    
    bool check0 = true;
    int size = str.length();
    
    for(auto ch : str) {
        if (ch != '0') {
         
            check0 = false;
            break;
        }
    }
    
    if(size == 1 || check0)
        return true;
    
    int mid = size / 2;
    string left = str.substr(0, mid);
    string right = str.substr(mid + 1);
    
    if(str[mid] == '1' && search(left) && search(right))
        return true;
    else
        return false;
}

vector<int> solution(vector<long long> numbers) {
    
    vector<int> answer;
    
    for(auto number : numbers) {
        
        string str = "";
        while(number) {
            
            long long remain = number % 2;
            str = to_string(remain) + str;
            number /= 2;
        }
        
        int idx = 2, size = str.length();
        
        while(1) {
            
            if(size <= idx - 1)
                break;
            
            idx *= 2;
        }
        
        for(int i = 1; i < idx - size; i++) {
            
            str = "0" + str;
        }
        
        if(search(str))
            answer.push_back(1);
        else
            answer.push_back(0);
    }
    
    return answer;
}