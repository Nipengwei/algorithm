# leetcode

## 1. [两数之和](https://leetcode-cn.com/problems/two-sum/)

**想法：**
数组是无序的，首先想到的是数组排序然后用二分搜索。但问题是排序过后下标也乱了，由下标联想到应使用**hashmap**。在新建的哈希表中搜索`target - num`的值

[code](https://github.com/Nipengwei/algorithm/blob/master/leetcode/code1.py)

## 2. [两数相加](https://leetcode-cn.com/problems/add-two-numbers/)

[code](https://github.com/Nipengwei/algorithm/blob/master/leetcode/code2.py)

## 3. [无重复字符的最长子串](https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/)
`sliding window`

**想法：**
用hashmap记录每个字符最后一次出现的位置，若遍历的字符已经存在hashmap中，则将子字符串的起始位置移到记录位置的后一位，开始计算新的子串

[code](https://github.com/Nipengwei/algorithm/blob/master/leetcode/code3.py)

## 5. [最长回文子串](https://leetcode-cn.com/problems/longest-palindromic-substring/submissions/)

**想法：**
1. 常规动态规划解法，复杂度$O(n^2)$
[code](https://github.com/Nipengwei/algorithm/blob/master/leetcode/code5.py)

## 7. [整数反转](https://leetcode-cn.com/problems/reverse-integer/submissions/)

[code](https://github.com/Nipengwei/algorithm/blob/master/leetcode/code7.py)

## 9. [回文数](https://leetcode-cn.com/problems/palindrome-number/)

**想法：**
将整数反转进行至一半即可

[code](https://github.com/Nipengwei/algorithm/blob/master/leetcode/code9.py)

## 10. [Z字型变换](https://leetcode-cn.com/problems/zigzag-conversion/)

**想法：**
创建n行空字符串，遍历时根据规律确定每个字符属于的行数。

[code](https://github.com/Nipengwei/algorithm/blob/master/leetcode/code10.py)

## 11. [最大子序和](https://leetcode-cn.com/problems/maximum-subarray/)

**想法：**
贪心算法，如果当前子集的和为负，则从当前元素重新开始计算子集。

[code](https://github.com/Nipengwei/algorithm/blob/master/leetcode/code11.py)

## 12. [反转链表](https://leetcode-cn.com/problems/reverse-linked-list/)

[code](https://github.com/Nipengwei/algorithm/blob/master/leetcode/code12.py)

## 13. [反转链表 II](https://leetcode-cn.com/problems/reverse-linked-list-ii/)

[code](https://github.com/Nipengwei/algorithm/blob/master/leetcode/code13.py)

## 14. [二叉树的最大深度](https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/)

[code](https://github.com/Nipengwei/algorithm/blob/master/leetcode/104.二叉树的最大深度.js)

## 15. [平衡二叉树](https://leetcode-cn.com/problems/balanced-binary-tree/)

[code](https://github.com/Nipengwei/algorithm/blob/master/leetcode/110.平衡二叉树.js)

## 16. [二叉树中的最大路径和](https://leetcode-cn.com/problems/binary-tree-maximum-path-sum/)

[code](https://github.com/Nipengwei/algorithm/blob/master/leetcode/124.二叉树中的最大路径和.js)

## 17. [二叉树的最近公共祖先](https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/)

[code](https://github.com/Nipengwei/algorithm/blob/master/leetcode/236.二叉树的最近公共祖先.js)

## 18. [二叉树的层序遍历](https://leetcode-cn.com/problems/binary-tree-level-order-traversal/)

[code](https://github.com/Nipengwei/algorithm/blob/master/leetcode/102.二叉树的层序遍历.js)