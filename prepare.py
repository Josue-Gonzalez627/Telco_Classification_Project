import pandas as pd
import numpy as np
import os
import warnings

import matplotlib.pyplot as plt
import env
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

plt.style.use(
    "https://github.com/dhaitz/matplotlib-stylesheets/raw/master/pitayasmoothie-dark.mplstyle"
)
pd.set_option("display.max_colwidth", 200)
warnings.filterwarnings("ignore")

def prep_telco(df):
    '''
    Drops some columns that have been brought over from the joins that are not needed. 
    Also replaces empty space values with 0.0 to give it a value.
    Filled null values with 'No internet service' because that's what it was originally
    supposed to represent.
    '''
    df = df.drop(columns = ['payment_type_id','internet_service_type_id','contract_type_id'])
    df.internet_service_type = df.internet_service_type.fillna('No internet service')
    df.total_charges = df.total_charges.str.replace(' ', '0.0')
    return df

def splitting_data(df, col, seed=123):
    '''
    Just like the splitting Titanic function but it can be used for any df now!
    must provide the df and column. Does not clean it though
    '''

    #first split
    train, validate_test = train_test_split(df,
                     train_size=0.6,
                     random_state=seed,
                     stratify=df[col]
                    )
    
    #second split
    validate, test = train_test_split(validate_test,
                                     train_size=0.5,
                                      random_state=seed,
                                      stratify=validate_test[col]
                        
                                     )
    return train, validate, test


def preprocess_telco(train_df, val_df, test_df):
    '''
    preprocess_telco will take in three pandas dataframes
    of our telco data, expected as cleaned versions of this 
    telco data set (see documentation on acquire.py and prepare.py)
    
    output:
    encoded, ML-ready versions of our clean data, with 
    columns sex and embark_town encoded in the one-hot fashion
    return: (pd.DataFrame, pd.DataFrame, pd.DataFrame)
    '''
    # with a looping structure:
    # go through the three dfs, set the index to customer id
    for df in [train_df, val_df, test_df]:
        df = df.set_index('customer_id')
        df['total_charges'] = df['total_charges'].astype(float)
    # initialize an empty list to see what needs to be encoded:
    encoding_vars = []
    # loop through the columns to fill encoded_vars with appropriate
    # datatype field names
    for col in train_df.columns:
        if train_df[col].dtype == 'O':
            encoding_vars.append(col)
    encoding_vars.remove('customer_id')
    # initialize an empty list to hold our encoded dataframes:
    encoded_dfs = []
    for df in [train_df, val_df, test_df]:
        df_encoded_cats = pd.get_dummies(
            df[encoding_vars],
              drop_first=True).astype(int)
        encoded_dfs.append(pd.concat(
            [df,
            df_encoded_cats],
            axis=1).drop(columns=encoding_vars))
    return encoded_dfs

def compute_class_metrics(y_train, y_pred):
    '''
    Will provide the confusion matrix with the pd.crosstab and label in 'counts'.
    Uses 'counts.iloc' to label each point in the matrix as TP, TN, FP, or FN.
    
    Using the variables and formulas for accuracy, TPR, FPR, TNR, FNR, precision, F1 score, 
    support_pos, and support_neg, will print out the metrics!
    '''
    counts = pd.crosstab(y_train, y_pred)
    TP = counts.iloc[1,1]
    TN = counts.iloc[0,0]
    FP = counts.iloc[0,1]
    FN = counts.iloc[1,0]
    
    
    all_ = (TP + TN + FP + FN)

    accuracy = (TP + TN) / all_

    TPR = recall = TP / (TP + FN)
    FPR = FP / (FP + TN)

    TNR = TN / (FP + TN)
    FNR = FN / (FN + TP)

    precision =  TP / (TP + FP)
    f1 =  2 * ((precision * recall) / ( precision + recall))

    support_pos = TP + FN
    support_neg = FP + TN
    
    print(f"Accuracy: {accuracy}\n")
    print(f"True Positive Rate/Sensitivity/Recall/Power: {TPR}")
    print(f"False Positive Rate/False Alarm Ratio/Fall-out: {FPR}")
    print(f"True Negative Rate/Specificity/Selectivity: {TNR}")
    print(f"False Negative Rate/Miss Rate: {FNR}\n")
    print(f"Precision/PPV: {precision}")
    print(f"F1 Score: {f1}\n")
    print(f"Support (0): {support_pos}")
    print(f"Support (1): {support_neg}")