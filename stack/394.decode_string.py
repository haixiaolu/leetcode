def decodeString(s: str) -> str:
    # create assistant stack
    stack = []
    res = ""
    multi = 0
    # 遍历字符串s中的每个字符
    for c in s:
        # 当c为 [ 时， 将但前multi和res入栈， 并分别设置为0
        if c == "[":
            stack.append([multi, res])
            res = ""
            multi = 0
        # 当c为 】 时， stack出栈， 拼接字符串res = last_rest + cur_multi * res
        elif c == "]":
            cur_multi, last_res = stack.pop()
            res = last_res + cur_multi * res
        # 当c为数字时， 将数字字符转化为数字multi
        elif "0" <= c <= "9":
            multi = multi * 10 + int(c)

        # 当字符为字母时， 在res后面添加c
        else:
            res += c
    return res


obj = decodeString(s="3[a]2[bs]")
print(obj)