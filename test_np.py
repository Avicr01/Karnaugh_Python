import numpy as np

R = 2
C = 2

a = [];
tmp = "";

for i in range(0, 4):
    tmp = int(input())
    a.append(tmp)

print(a)

entries = list(map(int, a))

# entries = list(map(int, a.split()))

matrix = np.array(entries).reshape(R, C)

for i in range(0, R):
    for j in range(0, C):
        print(matrix[i][j])
