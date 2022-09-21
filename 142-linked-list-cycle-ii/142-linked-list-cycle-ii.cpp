/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
ListNode *detectCycle(ListNode *head) {
        vector<ListNode*> v;
        while(head){
            v.push_back(head);
            auto itr = find(v.begin(), v.end()-1, head);
            if (itr != v.end()-1)
                return *itr;
            head = head->next;
        }
        return NULL;
    }
};