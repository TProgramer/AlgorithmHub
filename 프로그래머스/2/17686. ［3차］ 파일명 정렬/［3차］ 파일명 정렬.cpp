#include <string>
#include <vector>
#include <algorithm>

using namespace std;

struct fileName {
    int index;
    string head;
    int number;
};

vector<fileName> folder;

bool cmp(fileName f1, fileName f2) {
    
    if(f1.head == f2.head) {
        
        if(f1.number == f2.number) return f1.index < f2.index;
        
        return f1.number < f2.number;
    }
    
    return f1.head < f2.head;
}

vector<string> solution(vector<string> files) {
    vector<string> answer;

    for(int i = 0; i < files.size(); i++) {
        
        vector<int> idx;
        
        for(int j = 0; j < files[i].size(); j++) {
            
            if('0' <= files[i][j] && files[i][j] <= '9') {
                
                idx.push_back(j);
            }
        }
        
        string head = "";
        for(int j = 0; j < idx[0]; j++) {
            
            head += tolower(files[i][j]);
        }
        
        string number = files[i].substr(idx[0], idx.size());

        fileName f;
        f.index = i;
        f.head = head;
        f.number = stoi(number);

        folder.push_back(f);
    }
    
    sort(folder.begin(), folder.end(), cmp);
    for(int i = 0; i < folder.size(); i++) {
        
        answer.push_back(files[folder[i].index]);
    }
    return answer;
}