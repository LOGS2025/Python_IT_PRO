import math
import numpy as np
from seaborn import xkcd_palette
from sklearn.linear_model import LinearRegression 


'''
Since the population of this 'District' dropped since 1980, we will only do the regression
from 2000 onward, where it looks like a stable growth has begun again, even though the population 
is still well below the 1980 census.
'''

def linear_regression_for_population(year_array,pop_per_year)->sklearn.LinearRegression:
    x = np.array(year_array).reshape((-1,1))
    y = np.array(pop_per_year)

    model = LinearRegression().fit(x,y)
    r_sq = model.score(x,y)

    print(f"coefficient of determination for the population growth taking 2000->2020: {r_sq}")
    return model

