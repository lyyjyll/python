from Office import DoExcel as de 
import pandas as pd
import numpy as np

df = pd.DataFrame(np.arange(1,13).reshape(3,4))
de.create_xlsx(df,'data')
df.columns = ['one','two','three','four']
df.index = ['Tom','Peter','Linux']
de.save2sheet(df,filename='Test')










