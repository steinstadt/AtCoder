N, K = map(int, input().split())
H_list = list(map(int, input().split()))

count = 0

if N<K:
    print(0)
else:
    # リストをソートする
    H_list = sorted(H_list, reverse=True)
    # 上位K位をスライスで削除
    H_list = H_list[K:]


    # リスト内の残りの数を合計
    count = sum(H_list)
    print(count)
