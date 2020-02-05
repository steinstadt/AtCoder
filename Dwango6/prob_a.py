# Falling Asleep

# prepare input
N = int(input()) # データ数
playlist = [] # プレイリスト
for i in range(N):
    s, t = input().split()
    t = int(t)
    playlist.append([s,t])
X = input() # 寝落ちした時の曲

# Xのある要素を線形探索 O(N)
p = 0
for i in range(N):
    if playlist[i][0]==X:
        p = i
        break

# 時間の集計
playlist = playlist[p+1:] # プレイリストのカット
time = 0
for i in playlist:
    time = time + i[1]

# 結果の出力
print(time)
