# Telco Churn Analysis
 
### Project Description
 
Telco, a telecommunications enterprise, provides a wide array of services catering to a diverse clientele. This project will go into the exploration of distinct features influencing customer churn. The goal is to ascertain whether these factors increase or decrease the probability of customers discontinuing their services.
 
### Project Goal
 
* Find out what is causing the customer churn at Telco.
* Construct a Machine Learning Model using classification algorithms that accurately predict customer churn.
* Enhance our understanding of which customer attributes contribute to or mitigate churn.
 
### Initial Thoughts
 
My initial hypothesis is that drivers of churn will likely involve unsatisfied customers. Telco Services, or the lack thereof, might influence customers to churn. Services like tech support, phone service, internet service type, or how much a customer is paying per month.

## The Plan
 
1. Aquire data from Codeup MYSQL Database
 
2. Prepare data
   * Create Engineered columns from existing data
 
3. Explore data in search of drivers of churn
   * Answer the following initial questions
       * Is churn independent of tech support?
       * Is churn independent of internet service type?
       * Is churn independent of phone service?
       * Are there variations in churn based on monthly charges?
      
4. Develop a Model to predict if a customer will churn or not
   * Use drivers identified in Explore to build predictive models of different types
   * Evaluate models on the train and validate data
   * Select the best model based on the highest accuracy
   * Evaluate the best model on test data
 
5. Draw conclusions
 
## **Data Dictionary**

| Feature | Definition |
|:--------|:-----------|
|customer_id|Unique identifier for each customer|
|gender|The gender of the customer (male,female)|
|senior_citizen|Indicates whether the customer is a senior citizen|
|partner|Indicates whether the customer has a partner|
|dependents|Indicates whether the customer has dependents|
|tenure|The duration in months that a customer has been with the service provider|
|phone_service|Indicates whether the customer subscribes to phone service|
|multiple_lines|Indicates whether the customer has multiple phone lines|
|internet_service|Indicates whether the customer subscribes to internet service|
|online_security|Indicates whether the customer has online security features|
|online_backup|Indicates whether the customer has online backup features|
|device_protection|Indicates whether the customer has device protection features|
|tech_support|Indicates whether the customer has technical support services|
|streaming_tv|Indicates whether the customer subscribes to streaming TV services|
|streaming_movies|Indicates whether the customer subscribes to streaming movie services|
|paperless_billing|Indicates whether the customer has opted for paperless billing|
|monthly_charges|The amount charged to the customer monthly |
|total_charges|The total charges incurred by the customer|
|churn|Indicates whether the customer has churned|
|contract_type|Type of contract subscribed by the customer (month-to-month, one-year, two-year)|
|internet_service_type|Type of internet service subscribed by the customer (DSL, fiber optic)|
|payment_type|The method of payment chosen by the customer (bank transfer, credit card, electronic check, mailed check)|
 
# Steps to Reproduce
1) Clone this repo.
2) If you have access to the Codeup MYSQL DB:
   - Save **env.py** in the repo that follows the "sample env.py file" format below.
   - Ensure the **env.py** has the appropriate database connection.
3) If you don't have access:
   - Request access from Codeup
   - Follow step 2 after obtaining access.
5) Run notebook.

**<ins>sample env.py file:</ins>**<br>
host = 'data.codeup.com'<br>
username = 'sample_username'<br>
password = 'sample_password'<br>

def get_db_url(database_name, host_name=host, password=password, username=username):<br>
&nbsp;&nbsp;&nbsp;&nbsp;return f'mysql+pymysql://{username}:{password}@{host_name}/{database_name}'

# Takeaways and Conclusions
* 
 
# Recommendations
* 
