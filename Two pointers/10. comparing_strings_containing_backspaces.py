# leetcode 844. Backspace String Compare
"""
Gieven two strings containing backspaces(#), check if the two strings are equal
"""


def backspace_compare(s, t):
    # use two pointers approach to compare the strings
    index1 = len(s) - 1
    index2 = len(t) - 1
    while index1 >= 0 or index2 >= 0:
        i1 = get_next_valid_char_index(s, index1)
        i2 = get_next_valid_char_index(t, index2)

        if i1 < 0 and i2 < 0:  # reach the end of both the strings
            return True
        if i1 < 0 or i2 < 0:  # reach the end of one of the string
            return False
        if s[i1] != s[i2]:  # check if the characters are equal
            return False

        index1 = i1 - 1
        index2 = i2 - 1
    return True


def get_next_valid_char_index(str, index):
    backspace_count = 0
    while index >= 0:
        if str[index] == "#":  # found a backspace character
            backspace_count += 1
        elif backspace_count > 0:
            backspace_count -= 1
        else:
            break

        index -= 1  # skip a backspace or a valid character
    return index


def main():
    print(backspace_compare("xy#z", "xzz#"))
    print(backspace_compare("xy#z", "xyz#"))
    print(backspace_compare("xp#", "xyz##"))
    print(backspace_compare("xywrrmp", "xywrrmu#p"))


main()