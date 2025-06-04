import sys
input = sys.stdin.readline

sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
parent_list = list(map(int, input().split()))

# 트리 구성
tree = [[] for _ in range(n + 1)]
for i in range(2, n + 1):
    parent = parent_list[i - 1]
    tree[parent].append(i)

in_time = [0] * (n + 1)
out_time = [0] * (n + 1)
order = 0

def dfs(node):
    global order
    order += 1
    in_time[node] = order
    for child in tree[node]:
        dfs(child)
    out_time[node] = order

dfs(1)

# 세그먼트 트리 구성
size = 1
while size <= n:
    size *= 2
seg = [0] * (2 * size)

# 세그먼트 트리 업데이트 (구간에 val 더하기)
def range_add(l, r, val):
    l += size - 1
    r += size - 1
    while l <= r:
        if l % 2 == 1:
            seg[l] += val
            l += 1
        if r % 2 == 0:
            seg[r] += val
            r -= 1
        l //= 2
        r //= 2

# 세그먼트 트리 단일 조회
def point_query(pos):
    pos += size - 1
    res = 0
    while pos > 0:
        res += seg[pos]
        pos //= 2
    return res

# 쿼리 처리
for _ in range(m):
    cmd = input().split()
    if cmd[0] == '1':
        i, w = int(cmd[1]), int(cmd[2])
        l = in_time[i]
        r = out_time[i]
        range_add(l, r, w)
    elif cmd[0] == '2':
        i = int(cmd[1])
        print(point_query(in_time[i]))
