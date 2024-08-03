A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
print("Union of A and B:", A.union(B))
print("Union of A and B:", A | B)
print("Intersection of A and B:", A.intersection(B))
print("Intersection of A and B:", A & B)
print("Difference of A and B:", A.difference(B))
print("Difference of A and B:", A - B)
print("Symmetric Difference of A and B:", A.symmetric_difference(B))
print("Symmetric Difference of A and B:", A ^ B)
print("Is A a subset of B?", A.issubset(B))
print("Is B a subset of A?", B.issubset(A))
print("Is A a superset of B?", A.issuperset(B))
print("Is B a superset of A?", B.issuperset(A))
print("Are A and B disjoint?", A.isdisjoint(B))