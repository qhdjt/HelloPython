import csv


def getAny(fileName="D.csv"):
    # 初始化变量
    data = []
    ranges = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]  # 可以根据需要添加更多的范围
    max_value = 0
    min_value = 99999
    total_value2 = 0  # 用于计算第二列的总和
    count_value2 = 0  # 用于计算第二列的数据数量
    with open(fileName, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            # 跳过标题行
            if row[0] == '当前磁盘使用量' and row[1] == '写入轮次':
                continue
                # 将字符串转换为浮点数和整数
            value1 = float(row[0])
            value2 = int(row[1])
            data.append((value1, value2))

            total_value2 += value2  # 累加第二列的值
            count_value2 += 1  # 记录第二列的数据数量
            if value2 > max_value:
                max_value = value2
            if value2 < min_value:
                min_value = value2
    # 计算每个范围的平均值
    for start in ranges:
        end = start + 10  # 每个范围为10，可以根据需要进行调整
        count = 0
        total = 0
        for value1, value2 in data:
            if start <= value1 <= end:
                count += 1
                total += value2
        if count > 0:
            average = total / count
            print("百分比区间： {}~{}% ->平均写入轮次:{}".format(start, end, average))
        else:
            print("没有数据在 {}~{}% 范围内".format(start, end))
    print("最大写入轮次:{}".format(max_value))
    print("最小写入轮次:{}".format(min_value))
    # 计算第二列的平均值
    average_value2 = total_value2 / count_value2
    print("平均写入轮次:{}".format(average_value2))


getAny(fileName="D.csv")
