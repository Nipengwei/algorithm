/*
 * @lc app=leetcode.cn id=102 lang=javascript
 *
 * [102] 二叉树的层序遍历
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number[][]}
 */
var levelOrder = function (root) {
    let result = [];
    if (!root) {
        return result;
    }
    let currentLevel = [root];
    while (currentLevel.length) {
        let n = currentLevel.length
        result.push([]);
        for (let i = 0; i < n; i++) {
            let node = currentLevel.shift();
            result[result.length-1].push(node.val);
            if (node.left) {
                currentLevel.push(node.left);
            }
            if (node.right) {
                currentLevel.push(node.right);
            }
        }
    }
    return result;
};
// @lc code=end

