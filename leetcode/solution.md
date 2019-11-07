# leetcode

## 1. [两数之和](https://leetcode-cn.com/problems/two-sum/)
`数组`

**想法：**
数组是无序的，第一眼看到想到的是数组排序然后用二分搜索。但问题是排序过后下标也乱了，由下标联想到应使用**hashmap**。在新建的哈希表中搜索`target - num`的值

[code](https://github.com/Nipengwei/algorithm/blob/master/leetcode/code1.py)

## 2. [两数相加](https://leetcode-cn.com/problems/add-two-numbers/)

`链表`

[code](https://github.com/Nipengwei/algorithm/blob/master/leetcode/code2.py)

## 3. [无重复字符的最长子串](https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/)

`sliding window`

**想法：**
用hashmap记录每个字符最后一次出现的位置，若遍历的字符已经存在hashmap中，则将子字符串的起始位置移到记录位置的后一位，开始计算新的子串

[code](https://github.com/Nipengwei/algorithm/blob/master/leetcode/code3.py)