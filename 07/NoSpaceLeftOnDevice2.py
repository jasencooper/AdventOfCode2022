# Find all of the directories with a total size of at most 100000. 
# What is the sum of the total sizes of those directories?
import sys, pandas as pd

# build up a list of directory names & sizes
# when looking at a file, detect current directory & add the filesize to that dir
# when looking at a navigation command, change the current directory accordingly
# .. means go up one
# 'string' means go into that sub-folder

input = open(sys.path[0] + '/input')
out2 = pd.DataFrame()
cur_dir = '/'
loop_count = 0                       # for testing, stop loop after limiter
limiter = 60                        # for testing, stop loop after limiter
file_sizes = pd.DataFrame()

for line in input:
    loop_count += 1                  # for testing, stop loop after limiter
    #if loop_count >= limiter: break  # for testing, stop loop after limiter

    if line[0:4] == '$ cd':
        
        dest_dir = line.split(' ')[-1].replace('\n', '') # captures string after rightmost space in line, minus newline
        #print("current:", cur_dir, "destination:", dest_dir)
        if dest_dir == '/':
            #print(line, "going home!")
            cur_dir = dest_dir

        elif dest_dir == '..':
            #print(line, 'going up!')
            cur_dir = cur_dir[0:cur_dir.rindex('/')] # remove trailing '/'
            cur_dir = cur_dir[0:cur_dir.rindex('/')+1] # remove string after last '/'
            #dest_dir = cur_dir.split('/')[-2]
            #print(dest_dir)

        else:
            #print(line, 'going down!')
            cur_dir = cur_dir + dest_dir + '/'
        #print("new:", cur_dir)
    
    elif line[0] != '$' and line[0:3] != 'dir':
        file_size = int(line.split(' ')[0])
        file_name = str(line.split(' ')[1].replace('\n', ''))

        dir_list =['/']
        dirs = cur_dir.split('/')
        dirs = [dir for dir in dirs if dir] # remove blanks
        loop_dir = cur_dir
        for dir in dirs: dir_list.append(dir)
        #print(dir_list)

        for dir in dir_list:
            file_sized = pd.DataFrame([file_size], columns = [loop_dir], index=[file_name])
            #print(dir_size)
            file_sizes = pd.concat([file_sizes, file_sized])
            if loop_dir != '/': 
                loop_dir = loop_dir[0:loop_dir.rindex('/')]
                loop_dir = loop_dir[0:loop_dir.rindex('/')+1]

file_sizes =  file_sizes.fillna(0)
dir_sizes = pd.DataFrame()
for column in file_sizes.columns:
    dir_size = pd.DataFrame([sum(file_sizes[column])], columns = ['dir_size'], index = [column])
    dir_sizes = pd.concat([dir_sizes, dir_size])

dir_sizes = dir_sizes.sort_values(by=['dir_size'], ascending=True)

total_used = dir_sizes['dir_size']['/']
total_avail = 70000000
total_free = total_avail - total_used
target_free = 30000000
min_delete = target_free - total_free

print(dir_sizes)
print("total_used:", total_used, "total_free:", total_free, "min_delete:", min_delete)

for size in dir_sizes.sort_values(by=['dir_size'], ascending=True)['dir_size']:
    if size >= min_delete: 
        print(size)
        break

