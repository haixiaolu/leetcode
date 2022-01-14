# simulation
def buddyString(s, goal):
    # 情形一
    if len(s) != len(goal):
        return False

    # 情形二: s == goal, s中没有某个单词的重复次数大于等于2
    if s == goal and len(set(s)) < len(s):
        return True

    # 情形三： s, goal差异的字符希表长度不等于2
    diff = ""
    for i in range(len(s)):
        if s[i] != goal[i]:
            diff += s[i] + goal[i]

        # 情形四： s, goal差异的字符下标长度 == 2， 但goal中差异的字符串交换位置后，不等于s
        if len(diff) > 4:
            return False
    return len(diff) == 4 and diff == diff[::-1]
