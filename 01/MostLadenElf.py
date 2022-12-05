import pandas as pd, numpy as np

# load dataframe from file names input
df = pd.read_csv('input', names = ['CaloriesPerItem'], skip_blank_lines = False)

# column definition: return row index if CaloriesPerItem is null
col =  df.apply(lambda row: df['CaloriesPerItem'].isnull() * df.index)

# add column to dataframe
df = df.assign(ElfID = col.values)

# replace ElfID 0s with NaN
df['ElfID'].replace(0, np.nan, inplace = True)

# backfill values into blanks
df['ElfID'].bfill(inplace = True)

# sum calories by ElfID
dfSum = df.groupby(['ElfID']).sum()

# Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?
MaxCalories = max(dfSum['CaloriesPerItem'])
print(MaxCalories)

# filter top 3
dfSumFiltered = dfSum.sort_values(by=['CaloriesPerItem'], ascending=False).head(n=3)

# Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total?
MaxNCalories = dfSumFiltered['CaloriesPerItem'].sum()
print(MaxNCalories)