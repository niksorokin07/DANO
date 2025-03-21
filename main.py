import pandas as pd
from IPython.display import display

df = pd.read_excel('avito_new_data_for_dano.xlsx')
display(df['price'] > 0)
