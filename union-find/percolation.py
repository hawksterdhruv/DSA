import random
from union_find import UnionFind

X = 20
Y = 15
P = 0.54 # probality of OPEN

# for _ in range(10):
mat = []
uf = UnionFind(X * Y + 2)

for y in range(Y * X):
    # mat.append([])
    # for x in range(X):
    mat.append("\u2588")

for i in range(X * Y):
    # if X * (Y - 1) <= i < X * Y:
    #     print(i)
    if random.choices([False, True], weights=[100 * (1 - P), 100 * P])[0]:
        mat[i] = " "
        # First ROW
        if X > i >= 0:
            uf.union(i, X * Y)
        elif X * (Y - 1) <= i < X * Y:
            # print(i)
            uf.union(i, X * Y + 1)
            # Above Row
            if i - X > 0 and mat[i - X] == " ":
                uf.union(i, i - X)
        else:
            # Above Row
            if i - X > 0 and mat[i - X] == " ":
                uf.union(i, i - X )

            # Left Block
            if i - 1 > 0 and int((i - 1) / X) == int(i / X) and mat[i - 1] == " ":
                uf.union(i, i - 1)

print("\n".join(["".join(mat[i * X: i * X + X]) for i in range(Y)]))
print(uf.connected(X*Y, X * Y + 1, display=True))
print()
# while (k := input()) != "n":
#     print(uf.connected(0, int(k) + 1, display=True))
# input()
# for x in range(X):
#     for y in range(Y):
#         print(mat[x][y], end="")
#     print()
