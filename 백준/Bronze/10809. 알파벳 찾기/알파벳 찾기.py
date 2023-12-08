s = input()

alpha = [-1] * 26

for c in s:
    alpha[ord(c)-97] = s.index(c)

print(*alpha)