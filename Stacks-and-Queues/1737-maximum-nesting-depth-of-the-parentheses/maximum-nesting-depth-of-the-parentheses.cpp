class Solution {
public:
    int maxDepth(string s) {
        int count = 0 , maxx = 0 ;
        for(int i = 0 ; i < s.size() ; i++){
            if (s[i] == '('){
                count++;
            }
            else if (s[i] == ')') {
                count--;
            }
            if (count > maxx){
                maxx = count;
            }
        }
        return maxx;
    }
};