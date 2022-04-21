import random

c = 0
curent_floor = 0
count = 0
totalPlay = 0

# số lần chạy là 10000000
for i in range(10000000):

    count += 1
    # số chấm khi tung con xúc xắc
    a = random.randint(1, 6)

    # khi số chấm là: 1, 2
    if (1 <= a) and (a <= 2):
        # kiểm tra xem có ở tầng triệt hay không
        if (curent_floor > 0):
            curent_floor = curent_floor - 1

    # khi số chấm là: 3, 4, 5
    if (3 <= a) and (a <= 5):
        curent_floor = curent_floor + 1

    # khi số chấm là: 6
    if (a == 6):
        curent_floor = curent_floor + random.randint(1, 6)

    # khả năng phải đi xuống tầng triệt để đi lại
    if (random.randint(1, 1000) == 1):
        curent_floor = 0

    # kiểm tra thắng cuộc(Khi thắng thì phải reset tất cả về 0 và tính là 1 lượt chơi)
    if (curent_floor >= 60) and (count <= 100):
        count = 0
        curent_floor = 0
        totalPlay += 1
        c = c+1
    # kiểm tra thua cuộc(Khi thua phải reset tất cả về 0 và tính là 1 lượt chơi)
    if (curent_floor < 60) and (count > 100):
        count = 0
        curent_floor = 0
        totalPlay += 1


print(c/totalPlay)
