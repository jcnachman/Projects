

import pandas as pd
import numpy as np





def rename_columns_mta(df):
    df.rename(columns={'EXITS                                                               ':'EXITS', 'C/A':'CA'}, inplace=True)



def change_linename_to_set(df):
    df['LINENAMESET'] = pd.Series([set(df.LINENAME[i]) for i in range(len(df.LINENAME))])


def add_datetime_to_mta(df):
    df['DATETIME'] = df.DATE+' '+df.TIME
    df['DATETIME'] = pd.to_datetime(df['DATETIME'],format='%m/%d/%Y %H:%M:%S')


## DON'T USE THIS IT'S SLOW
def add_ins_outs_loop(df):
    df['INS'] = 0
    df['OUTS'] = 0
    for i, row in df.iterrows():
        if i == 0: continue
        if df['C/A'][i] == df['C/A'][i-1] and df['UNIT'][i] == df['UNIT'][i-1] and df['SCP'][i] == df['SCP'][i-1]:
            df['INS'][i] = row.ENTRIES - df.loc[i-1].ENTRIES
            df['OUTS'][i] = row.EXITS - df.loc[i-1].EXITS
            print("row "+i+" done")


# USE THIS INSTEAD
def add_ins_outs_to_df(df):
    mask = df.duplicated(['CA', 'UNIT', 'SCP', 'STATION'])
    df['INS'] = np.where(mask, df['ENTRIES'] - df['ENTRIES'].shift(1), np.nan)

