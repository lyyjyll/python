import pandas as pd
from pandas.core.reshape.concat import concat
import pathlib2 as pl2
from pyecharts import options as opts
from pyecharts.charts import Map, Timeline
import numpy as np


df = pd.read_csv('./data_combine.csv',encoding='utf-8')
df_area = df.iloc[:,1:3]
df_year = df.iloc[:,[-1]]
df_new = concat([df_area,df_year], axis = 1)
df_end = df_new.groupby(by=['year'])


tl = Timeline()
for i in range(2016, 2020):
    map0 = (
        Map()
        .add("", [list(z) for z in zip([provinve[:2] for provinve in np.array(df_end.get_group(i).iloc[1:,[0]]).flatten().tolist()],np.array(df_end.get_group(i).iloc[1:,[1]]).astype('int').flatten().tolist())], "china")  # 以列表形式存放数据
        .set_global_opts(
            title_opts=opts.TitleOpts(title="Map-{}年某些数据".format(i)),
            visualmap_opts=opts.VisualMapOpts(max_=85000),
        )
    )
    tl.add(map0, "{}年".format(i))
tl.render_notebook()




