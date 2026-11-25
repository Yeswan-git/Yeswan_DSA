class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        int n1 , n2;
        n1 = word1.size();
        n2 = word2.size();
        int i = 0 , j = 0;
        std::string  res = "" ;
        while (i < n1 && j < n2) {
            res += word1[i];
            res += word2[j];
            i++;
            j++;
        }
        while (i < n1){
            res += word1[i];
            i++;
        }
        while (j < n2){
            res += word2[j];
            j++;
        }
        return res;
    }
};