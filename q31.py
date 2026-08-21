def intersect(a,b):
    return sorted(set(a) & set(b))
a = {4,5,6,7}
b = {6,7,8,9}
print(intersect(a,b))