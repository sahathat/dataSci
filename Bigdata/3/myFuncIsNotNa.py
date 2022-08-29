def summary_table_not_na(df):
    import pandas as pd
    df_isna = df.count() - df.isna().sum()
    isna_per = round((df_isna/df.shape[0])*100,2)
    summary_na = pd.concat([df_isna[df_isna<len(df)],isna_per[isna_per<100]],axis=1)
    col1 = 'is Not Na'
    col2 = '%'
    summary_na.columns = [col1,col2]
    summary_na = summary_na[summary_na[col2] < 100]
    summary_na = summary_na.sort_values(col1,ascending=False)
    print(summary_na)