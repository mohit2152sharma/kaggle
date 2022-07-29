from tabula import read_pdf
import pandas as pd

def concat_df(dflist):
    cols = dflist[0].columns
    # check if first row is empty or not
    dfs = []
    for df in dflist:
        df.columns = cols
        dfs.append(df)
    
    return pd.concat(dfs)

# read news paper ad spends
tables = read_pdf('./india-govt-ad-spends/source/Lok_Sabha_Question_No_2053.pdf', pages='all')

# newspaper pages are from: 1 to 108
# television pages are from: 109 to 115
# online pages are from: 116 to 119

newspaper = concat_df(tables[0:107])
television = concat_df(tables[108:114])
online = concat_df(tables[115:118])





newspaper.to_csv('./india-govt-ad-spends/cleaned/newspaper_ad_spend.csv')
television.to_csv('./india-govt-ad-spends/cleaned/television_ad_spend.csv')
online.to_csv('./india-govt-ad-spends/cleaned/online_ad_spend.csv')
