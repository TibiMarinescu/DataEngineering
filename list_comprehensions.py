"""Let's learn about list comprehensions! You are given three integers  and  representing the dimensions of a cuboid along with an integer . Print a list of all possible coordinates given by  on a 3D grid where the sum of  is not equal to . Here, . Please use list comprehensions rather than multiple loops, as a learning exercise.

Example




All permutations of  are:
.

Print an array of the elements that do not sum to .


Input Format

Four integers  and , each on a separate line.

Constraints

Print the list in lexicographic increasing order."""
if __name__ == '__main__':
    x = int(raw_input())
    y = int(raw_input())
    z = int(raw_input())
    n = int(raw_input())
g = []
for i in range(0,x+1):
    for j in range(0,y+1):
        for k in range(0,z+1):
            perm_1 = i
            perm_2 = j
            perm_3 = k
            if (perm_1+perm_2+perm_3)!=n:
                if [perm_1, perm_2, perm_3] not in g:
                    g.append([perm_1, perm_2, perm_3])
print(g)
