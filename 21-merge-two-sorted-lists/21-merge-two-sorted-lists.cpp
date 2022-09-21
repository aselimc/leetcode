/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
ListNode *mergeTwoLists(ListNode *list1, ListNode *list2)
    {   
        if (list1 == nullptr) return list2;
        else if (list2 == nullptr) return list1;
        
        ListNode *output= new ListNode();
        ListNode *head = output;
        while ((list1 != nullptr && list2 != nullptr))
        {
            if ((list1->val < list2->val) && (list1->next != nullptr))
            {
                ListNode *temp= new ListNode(list1->val);
                output->next = temp;
                list1 = list1->next;
            }
            else if ((list2->val <= list1->val) && (list2->next != nullptr))
            {
                ListNode *temp= new ListNode(list2->val);
                output->next = temp;
                list2 = list2->next;
            }
            else if ((list1->val < list2->val) && (list1->next == nullptr))
            {
                ListNode *temp= new ListNode(list1->val);
                output->next = temp;
                list1 = list1->next;
                output = output->next;
                while (list2->next != nullptr)
                {
                    ListNode *temp= new ListNode(list2->val);
                    output->next = temp;
                    list2 = list2->next;
                    output = output->next;
                }
                    ListNode *temp2= new ListNode(list2->val);
                    output->next = temp2;
                    break;
            }
            else if ((list2->val <= list1->val) && (list2->next == nullptr))
            {
                ListNode *temp= new ListNode(list2->val);
                output->next = temp;
                list2 = list2->next;
                output = output->next;
                while (list1->next != nullptr)
                {
                    ListNode *temp= new ListNode(list1->val);
                    output->next = temp;
                    list1 = list1->next;
                    output = output->next;
                }
                    ListNode *temp2= new ListNode(list1->val);
                    output->next = temp2;
                    break;
            }
            else break;
            output = output->next;
        };
        return head->next;
        }
};