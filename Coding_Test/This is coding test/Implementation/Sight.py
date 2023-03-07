h = int(input())
count = 0

# hour
for i in range(h + 1) :
    # minute
    for j in range(60) :
        # second
        for k in range(60) :
            # 3이 포함되면 + 1
            if '3' in str(i) + str(j) + str(k) :
                count += 1

print(count)