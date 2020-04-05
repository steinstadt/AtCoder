# Problem D - Lunlun Number

# input
K = int(input())

# initialization
num_queue = []
k = 1

# count
while True:
    if k>=1 and k<=9: # 1桁の場合
        num_queue.append(k)
        k += 1
    else: # 2桁以降の場合
        min_num = str(num_queue.pop(0))
        keta_1 = int(min_num[-1])
        if keta_1==0:
            for i in range(2):
                tmp = int(min_num + str(i))
                num_queue.append(tmp)
                k += 1
                if k>K:
                    break
        elif keta_1==9:
            for i in range(keta_1-1, keta_1+1):
                tmp = int(min_num + str(i))
                num_queue.append(tmp)
                k += 1
                if k>K:
                    break
        else:
            for i in range(keta_1-1, keta_1+2):
                tmp = int(min_num + str(i))
                num_queue.append(tmp)
                k += 1
                if k>K:
                    break
    if k>K:
        break

# output
print(num_queue[-1])
