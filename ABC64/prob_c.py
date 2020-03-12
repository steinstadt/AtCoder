# Problem C - Colorful Leaderboard

# input process
N = int(input())
a_list = list(map(int, input().split()))

# initialization
kanmuri_count = {
    "king": 0
}

# count process
for a in a_list:
    if a<400 and not "gray" in kanmuri_count:
        kanmuri_count["gray"] = 1
    elif a>=400 and a<800 and not "brown" in kanmuri_count:
        kanmuri_count["brown"] = 1
    elif a>=800 and a<1200 and not "green" in kanmuri_count:
        kanmuri_count["green"] = 1
    elif a>=1200 and a<1600 and not "cyan" in kanmuri_count:
        kanmuri_count["cyan"] = 1
    elif a>=1600 and a<2000 and not "blue" in kanmuri_count:
        kanmuri_count["blue"] = 1
    elif a>=2000 and a<2400 and not "yellow" in kanmuri_count:
        kanmuri_count["yellow"] = 1
    elif a>=2400 and a<2800 and not "orange" in kanmuri_count:
        kanmuri_count["orange"] = 1
    elif a>=2800 and a<3200 and not "red" in kanmuri_count:
        kanmuri_count["red"] = 1
    elif a>=3200:
        kanmuri_count["king"] += 1

# output process
cur_clount = len(kanmuri_count) - 1
ans = cur_clount + kanmuri_count["king"]
print("%d %d"%(max(cur_clount,1), ans))
