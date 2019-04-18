import pandas as pd

def transform_df_for_ML(df):
    
    # drop row id
    train_df = train_df.drop(columns=['row_id'])
    
    # keep columns
    keep_cat_cols = ['property_type_str','loan_purpose_str','preapproval_str','applicant_ethnicity_str','applicant_sex_str']
    keep_numeric_cols = ['loan_amount', 'applicant_income', '']
