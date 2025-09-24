import pandas as pd

paths = pd.read_csv('data/sample/paths_sample.csv')
mmm = pd.read_csv('data/sample/mmm_features_sample.csv')
pos = pd.read_csv('data/sample/pos_sales_sample.csv')

print('Loaded sample CSVs:')
for name, df in [('paths', paths), ('mmm_features', mmm), ('pos_sales', pos)]:
    print(f'  {name}:', df.shape)
