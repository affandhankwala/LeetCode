/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int maxLevelSum(TreeNode* root) {
        if (root == nullptr){
            return 0;
        }
        std::queue<TreeNode*> q;
        q.push(root);
        int current_level{1}, current_sum{0};
        int highest_sum_level{1}, highest_sum{-999999};

        while (q.size() > 0){
            size_t queue_length = q.size();
            for (int i = 0; i < queue_length; i ++){
                TreeNode* current = q.front();
                q.pop();
                if (current != nullptr){
                    // Append children
                    if (current->left){ q.push(current->left);}
                    if (current->right){ q.push(current->right);}

                    current_sum += current->val;
                }
            }
            if (current_sum > highest_sum) {
                highest_sum = current_sum;
                highest_sum_level = current_level;
            }
            current_sum = 0;
            current_level++;
        }
        return highest_sum_level;
    }
};