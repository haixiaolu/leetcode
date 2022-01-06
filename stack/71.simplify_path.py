# 分割字符串， 遇到【两个点】栈不为空的情况下， 弹出栈顶， 遇到【目录名】压入栈，/连接栈顶和栈底
class Solution:
    def simplifyPath(self, path: str):
        names = path.split("/")
        stack = []

        for name in names:
            if name == "..":
                if stack:
                    stack.pop()

            elif name and name != ".":
                stack.append(name)

        return "/" + "/".join(stack)


obj = Solution()
print(obj.simplifyPath(path="/home/"))
print(obj.simplifyPath(path="/../"))
