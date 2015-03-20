/*
this is a oj, which i understand an information error, then get a new infomation.
     1
    / \
  2     3
we will calcuate left=1+2=3, right=1+3=4, then the sum = left + right = 3 + 4 = 7.
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
                     sum = q_sum.front() + p->val;
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
                     sum = q_sum.front() + p->val;
                     q_sum.pop();
                 }
                 else
                     sum = p->val;
                 result += sum;
             }
             else if (p->left != NULL) {
                 if (!q_sum.empty()){
                     sum = q_sum.front() + p->val;
                     q_sum.pop();
                 }
                 else
                     sum = p->val;
                 q_sum.push(sum);
                 q.push(p->left);
             }
             else {
                 if (!q_sum.empty()){
                     sum = q_sum.front() + p->val;
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
