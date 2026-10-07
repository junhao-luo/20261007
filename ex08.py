count = 0

for x in range(41):
    y = 40 - x
    total_visits = 5*x + 8*y

    if x >= 12 and total_visits >= 250:
        print('甲：{} 天，乙：{} 天，總拜訪：{} 次'.format(
            x, y, total_visits
        ))
        count += 1

print('符合條件的組合數 = {}'.format(count))