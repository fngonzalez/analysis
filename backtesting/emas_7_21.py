import pandas as pd


#Leo el CSV y lo convierto en DataFrame
spy_csv = pd.read_csv('../../db/SPY.csv')
spy_df = pd.DataFrame(spy_csv)

spy_df.Date= pd.to_datetime(spy_df.Date)



print(spy_df.info())
