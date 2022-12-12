import sys, pandas as pd

# load dataframe from the file named input saved with this .py file
df = pd.read_csv(sys.path[0] + '/input', names = ['OpponentShape', 'Outcome'], sep = ' ')

# convert outcome letters to points
def OutcomePoints(row):
    if row['Outcome'] == 'X':
        return 0 # lose
    elif row['Outcome'] == 'Y':
        return 3 # draw
    elif row['Outcome'] == 'Z':
        return 6 # win

# add column with outcome points
df['OutcomePoints'] = df.apply(lambda row: OutcomePoints(row), axis=1)

# determine shape (and associated points) I should choose
def ShapePoints(row):
    if   row['OpponentShape'] == 'A' and row['Outcome'] == 'X':
        return 3 # opponent played rock & I need to lose: choose scissors
    elif row['OpponentShape'] == 'A' and row['Outcome'] == 'Y':
        return 1 # opponent played rock & I need to draw: choose rock
    elif row['OpponentShape'] == 'A' and row['Outcome'] == 'Z':
        return 2 # opponent played rock & I need to win:  choose paper

    elif row['OpponentShape'] == 'B' and row['Outcome'] == 'X':
        return 1 # opponent played paper & I need to lose: choose rock
    elif row['OpponentShape'] == 'B' and row['Outcome'] == 'Y':
        return 2 # opponent played paper & I need to draw: choose paper
    elif row['OpponentShape'] == 'B' and row['Outcome'] == 'Z':
        return 3 # opponent played paper & I need to win: choose scissors

    elif row['OpponentShape'] == 'C' and row['Outcome'] == 'X':
        return 2 # opponent played scissors & I need to lose: choose paper
    elif row['OpponentShape'] == 'C' and row['Outcome'] == 'Y':
        return 3 # opponent played scissors & I need to draw: choose scissors
    elif row['OpponentShape'] == 'C' and row['Outcome'] == 'Z':
        return 1 # opponent played scissors & I need to win: choose rock

# add column with shape points
df['ShapePoints'] = df.apply(lambda row: ShapePoints(row), axis=1)

# What would your total score be if everything goes exactly according to your strategy guide?
TotalScore = df['ShapePoints'].sum() + df['OutcomePoints'].sum() 

print(TotalScore)

