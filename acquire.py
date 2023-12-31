import pandas as pd
import numpy as np

import env
import os

def check_file_exists(filename, query, url):
    '''
    Args:
        filename (str): The name of the database
        query (str, optional): The SQL query to execute, 'SELECT * FROM...'
        url (env function): The  function in env.py file that connects to the SQL database.
        
        MUST have your own env.py file to replicate. Formatted as:
    
    def get_db_url(db, 
                   user=user, 
                   password=password, 
                   host=host):
        return (f'mysql+pymysql://{user}:{password}@{host}/{db}')
        
        
    As the name implies, this here is to see if the file(csv) we are calling/using exists AND what to do 
    if it doesn't exist. 
    If it doesn't exist, it will read the query using the url (env info) and makes it into a csv file!
    '''
    
    if os.path.exists(filename):
        print('this file exists, reading csv')
        df = pd.read_csv(filename, index_col=0)
    else:
        print('this file doesnt exist, read from sql, and export to csv')
        df = pd.read_sql(query, url)
        df.to_csv(filename)
        
    return df

def get_telco_data():
    '''
    Retrieves the telco dataframe. The MySQL query will return all columns from the customers table,
    with the three additional columns because of the joins using their ids.
    The check file function will assure the telco file exists and what to do if it doesn't.
    '''
    url = env.get_db_url('telco_churn')
    query = '''
    select *
    from customers
        join contract_types
            using (contract_type_id)
        join internet_service_types
            using (internet_service_type_id)
        join payment_types
            using (payment_type_id)
    '''
    
    filename = 'telco_churn.csv'

    #call the check_file_exists fuction 
    df = check_file_exists(filename, query, url)
    return df