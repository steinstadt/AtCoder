# Problem D - String Formation

# リストで処理が遅かったら、、、
# キューデータ構造を使おう!

from collections import deque

# input process
S = input().replace("\n", "")
S = deque(list(S))
Q = int(input()) # query number

# initialization
sento = 1

# process
for i in range(Q):
    query_num = input()
    # クエリが１の時
    if query_num[0]=="1":
        # 反転処理
        if sento==1:
            sento = 10
        elif sento==10:
            sento = 1
    elif query_num[0]=="2":
        n, f, c = query_num.split()
        f = int(f)
        if f==1: # 先頭追加処理
            # 先頭の位置によって変わる
            if sento==1:
                S.appendleft(c)
            elif sento==10:
                S.append(c)
        elif f==2: # 末尾追加処理
            if sento==1:
                S.append(c)
            elif sento==10:
                S.appendleft(c)

# output process
if sento==1:
    print("".join(S))
else:
    print("".join(list(S)[::-1]))
