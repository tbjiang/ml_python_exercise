import pandas as pd
from IPython.display import display

data = pd.read_csv("data.csv", header = None, idex_col = False,
	names = ['age', 'workclass', 'education', 'gender', 'hour-per-week', 'occupation', 'income'])
diplay(data.head())
