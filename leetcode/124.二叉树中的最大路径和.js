/*
 * @lc app=leetcode.cn id=124 lang=javascript
 *
 * [124] 二叉树中的最大路径和
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */
var maxPathSum = function (root) {
    return helper(root)[1]
};

var helper = function (root) {
    if (root == null) {
        return [-Infinity, -Infinity]
    }
    let leftPathSum = helper(root.left)
    let rightPathSum = helper(root.right)
    let maxPath = root.val + Math.max(0, leftPathSum[0], rightPathSum[0])
    let maxPathTwo = Math.max(
        maxPath,
        root.val + leftPathSum[0] + rightPathSum[0],
        leftPathSum[1],
        rightPathSum[1]
    )
    return [maxPath, maxPathTwo]
};
// @lc code=end

