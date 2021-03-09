/*
 * @lc app=leetcode.cn id=394 lang=javascript
 *
 * [394] 字符串解码
 */

// @lc code=start
/**
 * @param {string} s
 * @return {string}
 */
var decodeString = function (s) {
    let numStack = [];
    let strStack = [];
    let currentNum = 0;
    if (s === "") return "";

    for (let char of s) {
        if (isFinite(+char)) {
            currentNum = (+char) + currentNum*10;
        }
        else if (char === "[") {
            strStack.push("");
            numStack.push(currentNum);
            currentNum = 0;
        }
        else if (char === "]") {
            let n = numStack.pop();
            let str = strStack.pop();
            str = str.repeat(n);
            if (strStack.length == 0) strStack.push(str);
            else strStack[strStack.length - 1] += str;
        }
        else {
            if (strStack.length == 0) strStack.push(char);
            else strStack[strStack.length - 1] += char;
        }
    }

    return strStack[0];
};
// @lc code=end

