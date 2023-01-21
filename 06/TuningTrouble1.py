import sys

# loop thru input characters (max = len(signal) - 4) to create 4-digit substrings
# for each substring, check if characters are duplicated
# if characters are duplicated, move to the next starting character & check again
# if characters are not duplicated, end loop
# output = starting character + 4

signal = open(sys.path[0] + '/input').read()

marker_found = False

for n in range(len(signal)-4):
    if marker_found == True: break
    sub = signal[n:n+4]
    
    for c in sub:
        if sub.count(c) > 1:
            marker_found = False
            break
        
        marker_found = True
        output = n + 4

print(sub, output)
