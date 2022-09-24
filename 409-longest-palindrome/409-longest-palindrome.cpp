class Solution {
public:
    int longestPalindrome(string s) {
        int n = 0;
        vector<int> count(123, 0);
        for (char c : s){
            if (count[c-'A']==0){
                count[c-'A']++;
            }
            else{
                count[c-'A']--;
                n++;
            }
        }
        n *= 2;
        if (accumulate(count.begin(), count.end(), 0)==0){
            return n;
        }
        else{
            return n+1;
        }
    }
};