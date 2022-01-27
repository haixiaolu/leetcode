def find_permutation(str1, pattern):
    window_start = 0
    matched = 0
    char_frequency = {}

    # create HashMap,
    for char in pattern:
        if char not in char_frequency:
            char_frequency[char] = 0
        char_frequency[char] += 1

    # iterate through the string
    # the goal is to match all the characters from the 'char_frequency' with the current window
    # try to extend the range[window_start, window_end]
    for window_end in range(len(str1)):
        right_char = str1[window_end]
        # if the character being added matches a character
        if right_char in char_frequency:
            # decrement the frequency of matched character
            char_frequency[right_char] -= 1
            # if the character frequency becomes zeros, we got a match
            if char_frequency[right_char] == 0:
                matched += 1
        # if the number of character matched is equal to the pattern
        # we got required permutation
        if matched == len(pattern):
            return True

        # shrink the window by one character
        # if the window size is greater than the length of the pattern
        if window_end >= len(pattern) - 1:
            left_char = str1[window_start]
            window_start += 1
            # if the character going out was part of the pattern
            # put it back in the frequency HashMap
            if left_char in char_frequency:
                if char_frequency[left_char] == 0:
                    matched -= 1
                char_frequency[left_char] += 1

    return False


def main():
    print("Permutation exist: " + str(find_permutation("oidbcaf", "abc")))
    print("Permutation exist: " + str(find_permutation("odicf", "dc")))
    print("Permutation exist: " + str(find_permutation("bcdxabcdy", "bcdyabcdx")))
    print("Permutation exist: " + str(find_permutation("aaacb", "abc")))


main()
