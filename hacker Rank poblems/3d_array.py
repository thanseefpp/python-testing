'''
# input
1
1
1
2
# output
[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]

Print an array of the elements that do not sum to n==3.
'''



x = int(input())
y = int(input())
z = int(input())
n = int(input())

list_values = []
for i in range(0,x+1):
    for j in range(0,y+1):
        for k in range(0,z+1):
            if i+j+k != n:
                list_values.append([i,j,k])
            else:
                pass
print(list_values)

# print([[x, y, z] for x in range(n) for y in range(n) for z in range(n)])


