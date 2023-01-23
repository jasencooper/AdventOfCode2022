# Consider your map; how many trees are visible from outside the grid?

import sys

map = open(sys.path[0] + '/input').read().split('\n')
map = [m for m in map if m] # remove blank at end

# will create a map representing visible trees
vmap = []

# loop thru rows and columns, evaluating every cell
for r in range(len(map)):
    vrow = ''
    for c in range(len(map[r])):
        tree = map[r][c]
        left = map[r][0:c]
        right = map[r][c+1:len(map)]
        up = ''
        down = ''

        for row in range(r):
            up = up + map[row][c]

        for row in range(r + 1, len(map)):
            down = down + map[row][c]

        if r == 0 or r == len(map) - 1 or c == 0 or c == len(map[0]) - 1:
            #print(tree, "is visible")
            vrow += 'V'
        elif tree <= max(left) and tree <= max(right) and tree <= max(up) and tree <= max(down):
            #print(tree, "is not visible")
            vrow += '_'
        else:
            #print(tree, "is visible")
            vrow += 'V'
    vmap.append(vrow)

total_visible = 0
for vr in range(len(vmap)):
    print(vmap[vr])
    total_visible += vmap[vr].count('V')

print("total visible trees:", total_visible)
