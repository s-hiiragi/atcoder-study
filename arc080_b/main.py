# ref.
# https://atcoder.jp/contests/abc069/tasks/arc080_b
# https://atcoder.jp/contests/arc080/tasks/arc080_b
#
# 【競技プログラミング】花金AtCoder緑Diff精進【きりみんちゃん/VTuber】
# https://www.youtube.com/watch?v=-rad0cM5E_Y

W, H = [int(s) for s in input().split(" ")]
N = int(input())
colorNums = [int(s) for s in input().split(" ")]

def g(colorNums):
    for i, n in enumerate(colorNums, start=1):
        for __ in range(n):
            yield i

#for i in g(colorNums):
#    print(i)

it = iter(g(colorNums))

for i in range(H):
    a = [next(it) for __ in range(W)]
    if i % 2 == 1:
        a = reversed(a)
    for j in a:
        print(j, end=' ')
    print()
