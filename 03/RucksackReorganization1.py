import sys, pandas as pd

# load dataframe from the file named "input" which is saved with this .py file
rucks = pd.read_csv(sys.path[0] + '/input', names = ['AllItems'])

#print(rucks.head())

# for each line in df: 
# determine length of string
# split first column into two based on half of string length (compartment 1 and compartment 2)
# compare compartments to determine which item is in both; save this item
# convert the list of duplicate items into values
# sum the values

def ItemCount(row):
    return len(row['AllItems'])

rucks['ItemCount'] = rucks.apply(lambda row: ItemCount(row), axis=1)

def Compartment1(row):
    return row['AllItems'][0:row['ItemCount']//2]

rucks['Compartment1'] = rucks.apply(lambda row: Compartment1(row), axis=1)

def Compartment2(row):
    return row['AllItems'][row['ItemCount']//2:row['ItemCount']]

rucks['Compartment2'] = rucks.apply(lambda row: Compartment2(row), axis=1)

def DuplicateItem(row):
    for i in row['Compartment1']:
        if i in row['Compartment2']:
            return i

rucks['DuplicateItem'] = rucks.apply(lambda row: DuplicateItem(row), axis=1)

def DuplicateItemPriority(row):
    test_string = str(row['DuplicateItem'][0])
    if test_string.isupper() == True:
        print(test_string, test_string.isupper())
        return ord(test_string) - ord('A') + 27
    else:  
        print(test_string, test_string.isupper())
        return ord(test_string) - ord('a') + 1

rucks['DuplicateItemPriority'] = rucks.apply(lambda row: DuplicateItemPriority(row), axis=1)

print(rucks.head())

print(sum(rucks['DuplicateItemPriority']))
