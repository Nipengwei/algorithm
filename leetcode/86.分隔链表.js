/*
 * @lc app=leetcode.cn id=86 lang=javascript
 *
 * [86] 分隔链表
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} x
 * @return {ListNode}
 */
var partition = function (head, x) {
    if (!head) return null;
    let smaller = new ListNode(0);
    let bigger = new ListNode(0);
    const smallHead = smaller;
    const bigHead = bigger;

    while (head) {
        if (head.val < x) {
            smaller.next = head;
            smaller = smaller.next;
        }
        else {
            bigger.next = head;
            bigger = bigger.next;
        }
        head = head.next;
    }
    bigger.next = null;
    smaller.next = bigHead.next;
    return smallHead.next;
};
// @lc code=end

