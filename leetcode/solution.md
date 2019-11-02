# leetcode

[toc]

## 1. [两数之和](https://leetcode-cn.com/problems/two-sum/)

>给定一个整数数组 `nums` 和一个目标值 `target`，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
>你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

**示例：**
```python
给定 nums = [2, 7, 11, 15], target = 9
因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
```
**思路：**
数组是无序的，第一眼看到想到的是数组排序然后用二分搜索。但问题是排序过后下标也乱了，由下标联想到应使用**hashmap**。在新建的哈希表中搜索`target - num`的值

[code](https://github.com/Nipengwei/algorithm/blob/master/leetcode/code1.py)