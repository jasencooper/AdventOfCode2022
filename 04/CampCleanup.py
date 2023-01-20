import sys, pandas as pd

# pipe is used to list multiple separators: - and ,
# engine is specified as 'python' due to ParserWarning
df = pd.read_csv(sys.path[0] + '/input', names = ['startA', 'endA', 'startB', 'endB'], sep = '-|,', engine = 'python')

def ContainCheck(row):
    if row['startA'] <= row['startB'] and row['endA'] >= row['endB']:
        return 1 # A contains B
    elif row['startB'] <= row['startA'] and row['endB'] >= row['endA']:
        return 1 # B contains A
    else:
        return 0

df['ContainCheck'] = df.apply(lambda row: ContainCheck(row), axis=1)

print(sum(df['ContainCheck']))

def OverlapCheck(row):
    if   row['startA'] <= row['startB'] <= row['endA']:
        return 1
    elif row['startA'] <= row['endB']   <= row['endA']:
        return 1
    elif row['startB'] <= row['startA'] <= row['endB']:
        return 1
    elif row['startB'] <= row['endA']   <= row['endB']:
        return 1
    else:
        return 0

df['OverlapCheck'] = df.apply(lambda row: OverlapCheck(row), axis=1)

print(sum(df['OverlapCheck']))
