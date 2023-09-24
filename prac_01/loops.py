# A.
print("A. count in 10s from 0 to 100:")
for i in range(0, 101, 10):
    print(i, end=' ')
print()

# B.
print("B. count down from 20 to 1:")
for i in range(20, 0, -1):
    print(i, end=' ')
print()

# C. print n stars
n = int(input("C. Enter a number："))
for _ in range(n):
    print('*', end='')
print()

# D. print n lines of increasing stars
n = int(input("D. Enter a number："))
for i in range(1, n + 1):
    print('*' * i)

