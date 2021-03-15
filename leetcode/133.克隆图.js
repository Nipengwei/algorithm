/*
 * @lc app=leetcode.cn id=133 lang=javascript
 *
 * [133] 克隆图
 */

// @lc code=start
/**
 * // Definition for a Node.
 * function Node(val, neighbors) {
 *    this.val = val === undefined ? 0 : val;
 *    this.neighbors = neighbors === undefined ? [] : neighbors;
 * };
 */

/**
 * @param {Node} node
 * @return {Node}
 */
var cloneGraph = function (node) {
    const visited = {};

    function clone(node) {
        if (!node) return node;

        if (node.val in visited) {
            return visited[node.val];
        }

        let newNode = new Node(node.val, []);
        visited[node.val] = newNode;

        for (let neighbor of node.neighbors) {
            newNode.neighbors.push(clone(neighbor));
        }

        return newNode;
    };

    return clone(node);
};
// @lc code=end

