# Consider each tree on your map. What is the highest scenic score possible for any tree?

import sys

map = open(sys.path[0] + '/input').read().split('\n')
map = [m for m in map if m] # remove blank at end

max_scenic_score = 0

# loop thru rows and columns, evaluating every cell
# skipping first and last rows and columns since these will have a score of 0 in at least one direction
for r in range(1, len(map) - 1):
    for c in range(1, len(map[r]) - 1 ):
        tree = map[r][c]

        left_score = 0
        right_score = 0
        up_score = 0
        down_score = 0 

        for col in range(c - 1, -1, -1):
            left_score += 1
            if map[r][col] >= tree: break

        for col in range(c + 1, len(map[0])):
            right_score += 1
            if map[r][col] >= tree: break

        for row in range(r - 1, -1, -1):
            up_score += 1
            if map[row][c] >= tree: break
        
        for row in range(r + 1, len(map)):
            down_score += 1
            if map[row][c] >= tree: break
        
        scenic_score = left_score * right_score * up_score * down_score
        #print(tree, left_score, right_score, up_score, down_score, scenic_score)
        if scenic_score > max_scenic_score: max_scenic_score = scenic_score


print("max scenic score:", max_scenic_score)
# 291840
