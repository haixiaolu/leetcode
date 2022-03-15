def canFinish(numCourses, prerequisites):
    from collections import defaultdict, deque

    # 入度数组（列表， 保存所有课程的依赖课程总数）
    in_degree_list = [0] * numCourses
    # 关系表（字典， 保存所有课程与依赖课程的关系）
    relation_dict = defaultdict(list)
    for i in prerequisites:
        # 保存课程初始入度值
        in_degree_list[i[0]] += 1
        # 添加依赖它的后续课程
        relation_dict[i[1]].append(i[0])
    queue = deque()
    for i in range(len(in_degree_list)):
        # 入度为0的课程入列
        if in_degree_list[i] == 0:
            queue.append(i)
    # 队列值存储入度为0的课程， 也就是可以直接选修的课程
    while queue:
        current = queue.popleft()
        # 选修课程 -1
        numCourses -= 1
        relation_list = relation_dict[current]
        # 如果有依赖此课程的后续课程则更新入度
        if relation_list:
            for i in relation_list:
                in_degree_list[i] -= 1
                # 后续课程除去当前课程无其他依赖课程则丢入队列
                if in_degree_list[i] == 0:
                    queue.append(i)
    return numCourses