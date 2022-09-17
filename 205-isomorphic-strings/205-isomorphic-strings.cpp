class Solution {
public:
    bool unique(vector<int> &nums) {
        unordered_set<int> s;
        for (int num : nums) {
            if (num == -1) continue;
            if (s.count(num)) {
                return false;
            }
            s.insert(num);
        }
        return true;
    }
    bool isIsomorphic(string s, string t) {
        vector<int> count(256, 0);
        vector<int> s1 (256, -1);
        for (int i=0; i<s.size(); i++) {
            if (s1[t[i]] == -1) {
                s1[t[i]] = s[i];
            } else if (s1[t[i]] != s[i]) {
                return false;
            }
            count[s[i]]++;
            count[s1[t[i]]]--;
            if (count[s[i]] < 0) {
                return false;
            }
        }
        if (!unique(s1)) {
            return false;
        }
        return true;
    }
        
};