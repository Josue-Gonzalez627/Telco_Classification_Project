# Telco Churn Analysis
 
# Project Description
 
Telco, a telecommunications enterprise, provides a wide array of services catering to a diverse clientele. This project will go into the exploration of distinct features influencing customer churn. The goal is to ascertain whether these factors increase or decrease the probability of customers discontinuing their services.
 
# Project Goal
 
* Find out what is causing the customer churn at Telco.
* Construct a Machine Learning Model using classification algorithms that accurately predict customer churn.
* Enhance our understanding of which customer attributes contribute to or mitigate churn.
 
# Initial Thoughts
 
My initial hypothesis is that drivers of churn will likely involve unsatisfied customers. Telco Services, or the lack thereof, might influence customers to churn. Services like tech support, phone service, internet service type, or how much a customer is paying per month.

# The Plan
 
* Aquire data from Codeup MYSQL Database
 
* Prepare data
   * Create Engineered columns from existing data
 
* Explore data in search of drivers of churn
   * Answer the following initial questions
       * Is churn independent of tech support?
       * Is churn independent of internet service type?
       * Is churn independent of phone service?
       * Are there variations in churn based on monthly charges?
      
* Develop a Model to predict if a customer will churn or not
   * Use drivers identified in Explore to build predictive models of different types
   * Evaluate models on the train and validate data
   * Select the best model based on the highest accuracy
   * Evaluate the best model on test data
 
* Draw conclusions
 
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
2) Acquire the data from [Kaggle](https://www.kaggle.com/datasnaek/chess)
3) Put the data in the file containing the cloned repo.
4) Run notebook.
 
# Takeaways and Conclusions
* Upsets occur in 1/3 of games
* In games where the lower rated player moves first there is a 4% greater chance of an upset
* Games that are rated have a 3% higher chance of an upset
* Games with a "quick" time control (30 min or less) have about a 1 in 3 chance of upset
* Games with a "slow" time control (60 min or more) have about a 1 in 5 chance of upset
* The mean rating of players in a game is not a driver of upsets
* The difference in player rating is a driver of upsets
* A player's choice of opening is a driver of upsets, however its influence is complicated and I would need more time to discover what role it plays
 
# Recommendations
* To increase the skill intensity of a game add to the length of time players are able to consider their moves
* Based on the data longer time controls make it less likely for a less skilled player to beat a more skilled player
