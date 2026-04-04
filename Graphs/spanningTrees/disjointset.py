class DisJointSet:

    def __init__(self, n):
        self.rank = [0 for _ in range(n+1)]
        self.parent = [i for i in range(n+1)]
        self.size = [1 for _ in range(n+1)]


    def findUlP(self, node):

        if self.parent[node] == node:
            return node
        
        self.parent[node] = self.findUlP(self.parent[node])
        return self.parent[node]
    

    def unionByRank(self, u, v):
        ul_u = self.findUlP(u)
        ul_v = self.findUlP(v)

        if self.rank[ul_u] < self.rank[ul_v]:
            self.parent[ul_u] = ul_v
        elif self.rank[ul_v] < self.rank[ul_u]:
            self.parent[ul_v] = ul_u
        else:
            self.parent[ul_v] = ul_u
            self.rank[ul_u] += 1

    def unionBySize(self, u, v):
        ul_u = self.findUlP(u)
        ul_v = self.findUlP(v)

        if self.size[ul_u] < self.size[ul_v]:
            self.parent[ul_u] = ul_v
            self.size[ul_v] += self.size[ul_u]
        else:
            self.parent[ul_v] = ul_u
            self.size[ul_u] += self.size[ul_v]



ds1 = DisJointSet(7)
ds2 = DisJointSet(7)

ds1.unionByRank(1, 2)
ds1.unionByRank(2, 3)
ds1.unionByRank(4, 5)
ds1.unionByRank(6, 7)
ds1.unionByRank(5, 6)

if (ds1.findUlP(3) == ds1.findUlP(7)):
    print('Same')
else:
    print('Not same')

ds1.unionByRank(3, 6)
if (ds1.findUlP(3) == ds1.findUlP(7)):
    print('Same')
else:
    print('Not same')

ds2.unionBySize(1, 2)
ds2.unionBySize(2, 3)
ds2.unionBySize(4, 5)
ds2.unionBySize(6, 7)
ds2.unionBySize(5, 6)

if (ds2.findUlP(3) == ds2.findUlP(7)):
    print('Same')
else:
    print('Not same')

ds2.unionByRank(3, 6)
if (ds2.findUlP(3) == ds2.findUlP(7)):
    print('Same')
else:
    print('Not same')