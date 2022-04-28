import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LassoLars, TweedieRegressor
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.feature_selection import SelectKBest, RFE, f_regression, SequentialFeatureSelector


from wrangle import *

import warnings
warnings.filterwarnings("ignore")


#Set the plot chart size and font size
plt.rc('figure', figsize=(13, 7))
plt.style.use('seaborn-whitegrid')
plt.rc('font', size=12)


def question1(df):
      
    sns.barplot(data= df, y='number_of_instances', x='condition')
    plt.title('Number of Instances Vs. Condition')
    plt.xticks(rotation=90)
    plt.xlabel('')
    plt.show()

def question2():

    df = clean_data()
    train, validate, test = wrangle(df)

    stroke = train[(train.condition == 'Stroke')==True]
    stroke_state = stroke.groupby('state').sum().sort_values(by=['number_of_instances'], ascending=False)
    stroke_state = stroke_state.reset_index()

    sns.barplot(data=stroke_state,x='state', y='number_of_instances')
    plt.xticks(rotation=90)
    plt.show()

    tx_stroke = stroke[(stroke.state == 'TX')==True]
    tx_city = tx_stroke.groupby('city').sum().sort_values(by=['number_of_instances'])
    tx_city = tx_city.reset_index()
    
    sns.barplot(data=tx_city, x='city', y='number_of_instances')
    plt.xticks(rotation=90)
    plt.show()

def question3():

    df = clean_data()
    train, validate, test = wrangle(df)

    stroke = train[(train.condition == 'Stroke')==True]
    stroke_state = stroke.groupby('state').sum().sort_values(by=['number_of_instances'], ascending=False)
    stroke_state = stroke_state.reset_index()

    sns.barplot(data=stroke_state,x='state', y='number_of_instances')
    plt.xticks(rotation=90)
    plt.show()

    vt_stroke = stroke[(stroke.state == 'VT')==True]
    vt_city = vt_stroke.groupby('city').sum().sort_values(by=['number_of_instances'])
    vt_city = vt_city.reset_index()
    
    sns.barplot(data=vt_city, x='city', y='number_of_instances')
    plt.xticks(rotation=90)
    plt.show()

def question4():

    df = clean_data()
    train, validate, test = wrangle(df)

    stroke = train[(train.condition == 'Stroke')==True]
    stroke_state = stroke.groupby('state').sum().sort_values(by=['number_of_instances'], ascending=False)
    stroke_state = stroke_state.reset_index()

    stroke_region = stroke.groupby('cms_region').sum().sort_values(by=['number_of_instances'], ascending=False)
    stroke_region = stroke_region.reset_index()

    sns.barplot(data=stroke_region,x='cms_region', y='number_of_instances')
    plt.xticks(rotation=90)
    plt.show()


