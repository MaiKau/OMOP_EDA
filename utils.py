import pandas as pd

def add_total_and_pct(cross_df):
    df = cross_df.copy()
    df['row_total'] = df.sum(axis=1)
    col_total = df.sum(axis=0)
    df.loc['col_total'] = col_total

    df_row_pct = df.div(df['row_total'], axis=0) * 100
    df_row_pct = df_row_pct.round(1)
    df_col_pct = df.div(df.loc['col_total'], axis=1) * 100
    df_col_pct = df_col_pct.round(1)

    combined = pd.concat(
        [df.astype(int).add_suffix('_count'),
         df_row_pct.add_suffix('_row%'),
         df_col_pct.add_suffix('_col%')],
        axis=1
    )
    return combined
