import pandas as pd

df = pd.read_csv('examen.csv')
df.to_pickle('exam_types.pkl')