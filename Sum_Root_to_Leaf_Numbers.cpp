/*
Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

For example,

    1
   / \
  2   3
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.

Return the sum = 12 + 13 = 25.
*/

#include<iostream>
#include<queue>
using namespace std;


//Definition for binary tree
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    int sumNumbers(TreeNode *root) {
         
        return BFS(root);
    }

    int BFS(TreeNode *root)
    {
        int result = 0;
        
        if (root == NULL)
            return result;

        queue<TreeNode*> q;
        q.push(root);

        queue<int> q_sum;

        while(!q.empty())
        {
            int sum = 0;
            TreeNode* p = q.front();
            q.pop();

             if ((p->right != NULL) && (p->left != NULL)) {
                 if (!q_sum.empty()){
                     sum = q_sum.front()*10 + p->val;
                     q_sum.pop();
                 }
                 else
                     sum = p->val;
                 q_sum.push(sum);
                 q_sum.push(sum);
                 q.push(p->left);
                 q.push(p->right);
             }
             else if ((p->left == NULL) && (p->right == NULL)) {
                 if (!q_sum.empty()){
                     sum = q_sum.front()*10 + p->val;
                     q_sum.pop();
                 }
                 else
                     sum = p->val;
                 result += sum;
             }
             else if (p->left != NULL) {
                 if (!q_sum.empty()){
                     sum = q_sum.front()*10 + p->val;
                     q_sum.pop();
                 }
                 else
                     sum = p->val;
                 q_sum.push(sum);
                 q.push(p->left);
             }
             else {
                 if (!q_sum.empty()){
                     sum = q_sum.front()*10 + p->val;
                     q_sum.pop();
                 }
                 else
                     sum = p->val;
                 q_sum.push(sum);
                 q.push(p->right);
             }
        }

        return result;
    }
};


int main(int argc, char** argv)
{
    struct TreeNode* root = new TreeNode(1);
    struct TreeNode* p = new TreeNode(2);
    struct TreeNode* q = new TreeNode(3);
    root->left = p;
    root->right = q;

    Solution s;
    int res = s.sumNumbers(root);

    cout<<res<<endl;

    return 0;
}
