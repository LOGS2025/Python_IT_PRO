import math
import numpy as np
from seaborn import xkcd_palette
from sklearn.linear_model import LinearRegression 


'''
Since the population of this 'District' dropped since 1980, we will only do the regression
from 2000 onward, where it looks like a stable growth has begun again, even though the population 
is still well below the 1980 census.
'''

def linear_regression_for_population()->sklearn.LinearRegression:
    year_complete = [1980,1990,2000,2005,2010,2015,2020]
    year = [2000,2005,2010,2015,2020]
    pop_complete = [480_741.00,407_811.00,360_478.00,355_017.00,385_439.00,417_416.00,432_259.00]
    pop = [360_478.00,355_017.00,385_439.00,417_416.00,432_259.00]

    x = np.array(year).reshape((-1,1))
    y = np.array(pop)

    model = LinearRegression().fit(x,y)
    r_sq = model.score(x,y)

    print(f"coefficient of determination for the population growth taking 2000->2020: {r_sq}")
    return model

linear_regression_for_population()
