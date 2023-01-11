import sys, pandas as pd

# load dataframe from the file named input saved with this .py file
df = pd.read_csv(sys.path[0] + '/input', names = ['OpponentShape', 'MyShape'], sep = ' ')

# load dataframe converting XYZ to 123 & indicating outcomes
dfShape = pd.DataFrame({
    'MyShape':      ['X', 'Y', 'Z'],
    'ShapePoints':  [ 1 ,  2 ,  3 ], 
    'WinIf':        ['C', 'A', 'B'],
    'DrawIf':       ['A', 'B', 'C'],
    'LoseIf':       ['B', 'C', 'A']
})

# merge shape score and outcome indicator into main dataframe
df = pd.merge(
    left = df,
    right = dfShape,
    how = "inner"
)

# evaluate OpponentShape to determine outcome
def OutcomePoints(row):
    if row['OpponentShape'] == row['WinIf']:
        return 6
    elif row['OpponentShape'] == row['DrawIf']:
        return 3
    elif row['OpponentShape'] == row['LoseIf']:
        return 0

# add column with outcome points
df['OutcomePoints'] = df.apply(lambda row: OutcomePoints(row), axis=1)

# What would your total score be if everything goes exactly according to your strategy guide?
TotalScore = df['ShapePoints'].sum() + df['OutcomePoints'].sum() 

print(TotalScore)

