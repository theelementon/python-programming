#program to find common elements of a list

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

a = list(set(a))
print a
print b
j=0
for i in range(0,len(a),1):
        if(a[i] == b[j] for j in range(0,len(b),1)):
            print a[i]

#alternate
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

print set(a) & set(b)