# https://atcoder.jp/contests/arc001/tasks/arc001_3
# 斜めもダメということを忘れていた

import io

s1 = '''\
........
........
.......Q
........
..Q.....
........
.Q......
........
'''

s2 = '''\
.....Q..
.Q......
........
........
........
Q.......
........
........
'''

s = s2

c = []

with io.StringIO(s) as f:
    for line in f:
        c.append(list(line.strip()))

def print_map(c):
    for i in range(len(c)):
        print(' '.join(c[i]))

print('INPUT')
print_map(c)

i_s = list(range(8))
j_s = list(range(8))

for i in range(8):
    for j in range(8):
        if c[i][j] == 'Q':
            i_s.remove(i)
            j_s.remove(j)

def solve(i_s, j_s, points):
    for i in i_s:
        for j in j_s:
            if c[i][j] == '.':
                i_s2 = i_s.copy()
                j_s2 = j_s.copy()
                i_s2.remove(i)
                j_s2.remove(j)
                if len(i_s2) == 0 and len(j_s2) == 0:
                    return points + [(i, j)]
                ans = solve(i_s2, j_s2, points)
                if ans:
                    return ans + [(i, j)]
    return None

ans = solve(i_s, j_s, [])
if ans:
    for i,j in ans:
        c[i][j] = 'Q'
    print('Answer')
    print_map(c)
else:
    print('No Answer')
