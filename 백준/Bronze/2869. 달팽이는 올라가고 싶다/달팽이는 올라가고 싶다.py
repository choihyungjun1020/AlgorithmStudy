# v = 나무막대 높이
# b = 자는동안 이만큼 -
# a = 낮에 올라가는 +

# x일이 걸린다 -> x = x번 올라가고, x-1번 내려감
# a * x - b * (x-1) = V

# ax + bx - b = v
# ax - bx = v - b
# (a - b) * x
# x = (v - b) / (a - b)
a, b, v = map(int, input().split())

day = (v - b) / (a - b)

if day == int(day):
    print(int(day))
else:
    print(int(day)+1)
