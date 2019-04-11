import pandas as pd

def factor_int_column_with_keys(df, column_key, replace_dict):
    # map categories to somethign useful
    # don't edit underlying data when possible
    new_col_str = column_key + "_str"
    df[new_col_str] = df[column_key].astype(str)
    
    # limit replace to a single column 
    df[new_col_str] = df[new_col_str].replace(replace_dict)
    labels, levels = pd.factorize(df[new_col_str])
    
    #new_class_col = column_key + "_class"
    #df[new_class_col] = levels
    

def remove_cols_with_perc_missing_values(df, min_ratio):
    # remove columns with less than min_ratio of valid values
    # IE - remove any column that doesn't have at least 70% non-null values 
    df_filtered = df[[column for column in df if df[column].count() / len(df) >= min_ratio]]
    print('columns with less than ', min_ratio, ' non-null values: ')
    
   # print(df_filtered.head(5))
    # compare the original column list to new column list
    for column in df.columns:
        if column not in df_filtered.columns:
            print("'", column, "' removed.")
    #return df_filtered
    
    
def minMax_normalize_df_col(df, col_key):
    # normalize a single column
    c = df[col_key]
    df[col_key] = (c - c.min())/(c.max()-c.min())
    
def mean_normalize_df_col(df, col_key):
    # normalize a single column
    c = df[col_key]
    df[col_key] = (c - c.mean())/c.std()
    
    
# see if there's any significant difference ( +- 5% of 50% ) per category
def category_compare_to_classification_label(df, label_key, max_fields=10):
    for col in df.columns:
        # not helpful if there are too many unique columns
        num_unique = df[col].nunique()
        if num_unique < max_fields:
            print(pd.crosstab( df[col], df[label_key], normalize='index'))
        else:
            print(col , ' column has too many unique fields (',num_unique ,')')
        print('------')
              