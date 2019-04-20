import pandas as pd
import utilities
from sklearn.preprocessing import RobustScaler

def transform_df_for_ML(df):
    
    # drop row id
    #ddf = df.drop(columns=['row_id'])
    
    # loan_type
    loan_type_dict = {'1':'Conventional', '2':'FHA-Insured', '3':'VA-guarenteed', '4':'FSA/RHS'}
    utilities.factor_int_column_with_keys(df, 'loan_type', loan_type_dict)

    # property type
    property_type_dict = {'1':'1 to 4 Family - non manufactured', 
                          '2':'Manufactured Housing',
                          '3':'Multifamily'}
    utilities.factor_int_column_with_keys(df, 'property_type', property_type_dict)

    # loan purpose
    loan_purpose_dict = {'1':'Home purchase',
                          '2':'Home improvement',
                          '3':'Refinancing'}
    utilities.factor_int_column_with_keys(df, 'loan_purpose', loan_purpose_dict)

    # occupancy
    occupancy_dict = {'1':'Owner Occupied',
                      '2':'Not owner-occupied',
                      '3': None}
    utilities.factor_int_column_with_keys(df, 'occupancy', occupancy_dict)

    # preapproval
    preapproval_dict = {'1':'Requested',
                        '2':'Not Requested',
                        '3':None}
    utilities.factor_int_column_with_keys(df, 'preapproval', preapproval_dict)

    # applicant_ethnicity 
    app_ethnicity_dict = {'1':'Hispanic',
                      '2':'Not Hispanic',
                      '3':None,
                      '4':None,
                      '5':None}
    utilities.factor_int_column_with_keys(df, 'applicant_ethnicity', app_ethnicity_dict)

    # applicant_race 
    app_race_dict = {'1':'American Indian',
                    '2':'Asian',
                     '3':'African American',
                     '4':'Pacific Islander',
                     '5':'White',
                     '6':None,
                     '7':None,
                     '8':None}
    utilities.factor_int_column_with_keys(df, 'applicant_race', app_race_dict)

    # applicant_sex 
    app_gender_dict = {'1':'Male',
                       '2':'Female',
                       '3':None,
                       '4':None}
    utilities.factor_int_column_with_keys(df, 'applicant_sex', app_gender_dict)
    
    df['co_applicant'] = df['co_applicant'].astype(int)
    
    # keep columns
    keep_cat_cols = ['property_type_str','loan_purpose_str','preapproval_str','applicant_ethnicity_str','applicant_sex_str']
    keep_numeric_cols = [ 'minority_population_pct', 'tract_to_msa_md_income_pct', 'loan_amount', 'applicant_income', 'co_applicant',
                          'msa_md', 'ffiecmedian_family_income','minority_population_pct' ]
    
    subset_df = pd.DataFrame()
    
    for c in keep_cat_cols:
        subset_df[c] = df[c]
        
    # float columns to consider
    numeric_cols =[ 'loan_amount', 'applicant_income', 'population', 'ffiecmedian_family_income',
                   'number_of_owner-occupied_units', 'number_of_1_to_4_family_units']

    # use robust scaler for outlier numerics
    for col in numeric_cols:
     #   utilities.minMax_normalize_df_col(df, col)
        col_copy = df[[ col ]].copy()
        transformer = RobustScaler().fit( col_copy  )
        df[ col ] = transformer.transform( col_copy )
     
    # scale the numeric columns 
    for c in keep_numeric_cols:
        subset_df[c] = df[c]
        
    return subset_df
    
    
