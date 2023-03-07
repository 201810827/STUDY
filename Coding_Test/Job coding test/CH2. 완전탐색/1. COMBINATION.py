from itertools import combinations

arr = []
for _ in range(9) :
    arr.append(int(input()))

for i in combinations(arr, 7) :
    if sum(i) == 100 :
        for j in sorted(i) :
            print(j)
        break


# 9개 중 2개 고르기
# h = [int(input()) for _ range(9)]
# tot = sum(h)

# def solve() :
# for i in range(8) :
#   for j in range(i+1, 9) :
#       if tot - h[i] - h[j] == 100 :
#           for k in h :
#               if k != h[i] and k != h[j] :
#                   print(k)
#      return

# solve()