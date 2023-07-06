#include <set>
#include <vector>
#include <algorithm>
using namespace std;

int solution(vector<int> nums)
{
    set<int> checkDuplicate;
    
    for(auto num : nums)
        checkDuplicate.insert(num);
    
    int maximumSize = nums.size() / 2;
    int checkSize = checkDuplicate.size();
    return min(checkSize, maximumSize);
}