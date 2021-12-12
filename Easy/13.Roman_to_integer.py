"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D, M
I : 1
V : 5
X : 10
L : 50
C : 100
D : 500
M : 1000

For example , 2 is writtern as II in Roman numeral, just two one's added together. 12 is written as XII

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII
instead, the number four is written as IV. Because the one is before the five we subtract it making four
"""


"""
Approach: using dictionary

- the last letter is always added.
- except the last one, if one letter is less than its latter one, this letter is subtracted
"""


def romanToInt(s: str) -> int:
    roman = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}

    result = 0

    for i in range(0, len(s) - 1):
        if roman[s[i]] < roman[s[i + 1]]:
            result -= roman[s[i]]
        else:
            result += roman[s[i]]

    return result + roman[s[-1]]