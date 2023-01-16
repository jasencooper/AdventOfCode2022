import sys, pandas as pd

# load dataframe from the file named "input" which is saved with this .py file
rucks = pd.read_csv(sys.path[0] + '/input', names = ['AllItems'])

#print(rucks.head())

rucks['NextSack'] = rucks['AllItems'].shift(-1)
rucks['ThirdSack'] = rucks['AllItems'].shift(-2)
rucks = rucks.iloc[::3] # limit to every third row, to avoid duplicates

def DuplicateItem(row):
    for i in row['AllItems']:
        if i in row['NextSack'] and i in row['ThirdSack']:
            return i

rucks['DuplicateItem'] = rucks.apply(lambda row: DuplicateItem(row), axis = 1)

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
