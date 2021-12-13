"""
Question: Given a string s containing just the characters '(', ')', '{', '}', '[', ']'
          determine if the input string is valid
"""
"""
Approach: 栈

    - 遍历给定的字符串s， 当我们遇到一个左括号时， 我们会期望在后续的遍历中， 有一个相同类型的右括号将其闭合。  
      由于后遇到的左括号要先闭合，因此我们可以讲这个左括号放入栈顶。 
    - 当我们遇到一个右括号时， 我们需要将一个相同类型的左括号闭合。 此时， 我们可以取出栈顶的左括号并判断它们是否是相同类型的括号。
        -- 如果不是相同的类型， 或者栈中没有左括号， 那么字符串s无效， 返回False， 
        -- 为了快速判断括号的类型， 我们可以使用哈希表存储每一种括号，哈希表的键为右括号， 值为相同类型的左括号
    - 在遍历结束后， 如果战中没有左括号， 说明我们将字符串s中的所有左括号闭合， 返回True， 否则返回False

"""


def isValid(s: str) -> bool:
    # 如果是奇数， 直接返回False
    if len(s) % 2 == 1:
        return False

    pairs = {")": "(", "]": "[", "}": "{"}

    stack = list()

    for char in s:
        if char in pairs:
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()
        else:
            stack.append(char)

    return not stack


# Time: o(n)
# Space: O(n + |SUM|), 其中|SUM|表示字符集， 本题中字符串只包含6种括号， ｜SUM｜ = 6