import pandas as pd
import numpy as np


def wrangle():
    
    # Acquire data from csv
    df = pd.read_csv('inpatient_rehabilitation_facilities_12_2021/Inpatient_Rehabilitation_Facility-Conditions_Dec2021.csv')
    
    # clean columns
    df.columns = [column.lower().replace(' ', '_').replace('-','_') for column in df]
    
    # make count column easy to work with
    df.rename(columns={'count':'number_of_instances'}, inplace=True)
    df.number_of_instances.replace({'Less than 11':'10', 'Not Available':'0'}, inplace=True)
    df = df.astype({'number_of_instances':'int'})
    
    # drop unnecessary columns
    columns_to_drop = ['phone_number', 'address_line_1', 'address_line_2', 'facility_name', 'zip_code']
    df.drop(columns=columns_to_drop, inplace=True)
    
    # fill nulls with 0
    df = df.fillna(0)
    
    # return clean Dataframe
    return df