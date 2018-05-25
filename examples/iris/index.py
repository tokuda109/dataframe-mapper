
import os

import pandas as pd
from dfmapper import DataFrameMapper, FloatColumn, StrColumn

iris_df = pd.read_csv(os.path.join(os.getcwd(), 'iris.csv'))

class IrisDfm(DataFrameMapper):

    SepalLength = FloatColumn()
    SepalWidth = FloatColumn()
    PetalLength = FloatColumn()
    PetalWidth = FloatColumn()
    Name = StrColumn()

iris_dfm = IrisDfm(iris_df)

print(iris_dfm.validate())
