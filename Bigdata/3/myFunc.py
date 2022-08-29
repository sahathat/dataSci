def summary_table(df):
    import pandas as pd
    df_isna = df.isna().sum()
    isna_per = round((df_isna/df.shape[0])*100,2)
    summary_na = pd.concat([df_isna[df_isna>0],isna_per[isna_per>0]],axis=1)
    col1 = 'is Na'
    col2 = '%'
    summary_na.columns = [col1,col2]
    summary_na = summary_na[summary_na[col1] > 0]
    summary_na = summary_na.sort_values(col1,ascending=False)
    print(summary_na)
