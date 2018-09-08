M = [x for x in range(2, 62, 2)]
N = [x for x in range(3, 93, 3)]

print(len(set(M)))
print(len(set(N)))

M = set(M)
N = set(N)

print('M union N', M.union(N))
print('M intersection N', M.intersection(N))
print('M - N', M.difference(N))
print('N - M', N.difference(M))