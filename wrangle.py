import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split

def clean_data():
    
    # Acquire data from csv
    df = pd.read_csv('inpatient_rehabilitation_facilities_12_2021/Inpatient_Rehabilitation_Facility-Conditions_Dec2021.csv')
    
    # clean columns
    df.columns = [column.lower().replace(' ', '_').replace('-','_') for column in df]
    
    # make count column easy to work with
    df.rename(columns={'count':'number_of_instances'}, inplace=True)
    df.number_of_instances.replace({'Less than 11':'10', 'Not Available':'0'}, inplace=True)
    df = df.astype({'number_of_instances':'int'})

    # fill nulls with 0
    df = df.fillna(0)    

    # drop unnecessary columns
    columns_to_drop = ['phone_number', 'address_line_1', 'address_line_2', 'facility_name', 'zip_code']
    df.drop(columns=columns_to_drop, inplace=True)
    
    # change dtypes for region and footnote
    df= df.astype({'cms_region':'object', 'footnote':'object'})
    
    # return clean Dataframe
    return df

def wrangle(df):

    #create dummy columns
    dummy_df = pd.get_dummies(df[['state', 'condition']], dummy_na=False)
    
    #concatenate columns with original dataframe
    df = pd.concat([df,dummy_df], axis=1)

    #clean new columms
    df.columns = [column.lower().replace(' ', '_').replace('-','_') for column in df]

    #split data
    train_validate, test = train_test_split(df, test_size=.2, random_state=177)
    train, validate = train_test_split(train_validate, test_size=.3, random_state=177)

    #print statement and split shape
    print('data has been split')
    print(train.shape, validate.shape, test.shape)
    
    #return split data 
    return train, validate, test