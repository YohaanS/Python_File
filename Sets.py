
myset = set()

myset.add(1)
myset.add(2)
myset.add(3)

print(myset.pop())
myset.discard(9)
for i in myset:
    print(i)
if 2 in myset:
    print("Yes")    

print(myset)

odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}

u = odds.union(evens)
print(u)

i = evens.intersection(primes)
print(i)



setA = {1, 2, 3, 4, 5, 6}
setB = {1, 2, 3}
setC = {7, 8}
print(setB.issubset(setA))
print(setB.issuperset(setA))
print(setA.isdisjoint(setC))
diff = setB.difference(setA)
print(diff)
diff2 = setB.symmetric_difference(setA)
print(diff2)
setA.update(setB)
print(setA)
setA.intersection_update(setB)
print(setA)
setA = {1, 2, 3, 4, 5, 6}

setB = setA.copy()

setB.add(7)
print(setB)
print(setA)
setB = set(setA)
setB.add(7)
print(setB)
print(setA)

a = frozenset([1, 2, 3, 4])


print(a)