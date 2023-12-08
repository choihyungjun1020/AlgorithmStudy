b = [i+1 for i in range(30)]


for i in range(28):
    b.remove(int(input()))

print(*b, sep="\n")