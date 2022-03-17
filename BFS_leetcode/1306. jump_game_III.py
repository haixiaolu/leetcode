def canReach(arr, start):
    if arr[start] == 0:
        return True

    n = len(arr)
    visited = {start}
    q = collections.deque([start])

    while q:
        node = q.pop(0)
        # check if reach zero
        if arr[node] == 0:
            return True
        if arr[node] < 0:
            continue

        # check available next steps
        for i in [node + arr[node], node - arr[node]]:
            if 0 <= i < n and i not in visited:
                if arr[i] == 0:
                    return True
                q.append(i)
                visited.add(i)
        return False
