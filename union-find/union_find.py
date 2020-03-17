class UnionFind:
    def __init__(self, N):
        self.ar = list(range(N))
        self.size = [1] * N

    def union(self, a, b):
        if self.connected(a, b):
            return

        while self.ar[a] != a:
            a = self.ar[a]

        while self.ar[b] != b:
            b = self.ar[b]

        if self.size[a] < self.size[b]:
            self.ar[a] = b
            self.size[b] += 1
        else:
            self.ar[b] = a
            self.size[a] += 1

    def connected(self, a, b, display=False):

        while self.ar[a] != a:
            if display:
                print(a)
            a = self.ar[a]

        while self.ar[b] != b:
            if display:
                print(b)
            b = self.ar[b]

        return a == b
