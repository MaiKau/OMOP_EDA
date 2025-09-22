import pandas as pd
from .utils import add_total_and_pct

def analyze_observations(df_obs: pd.DataFrame, df_person: pd.DataFrame):
    results = {}
    df = pd.merge(df_obs, df_person, how='left', on='person_id')

    # 體重
    weight_df = df[df['unit_source_value'] == 'kg'].copy()
    bins = [0, 50, 60, 70, 80, 90, 100, 120, float('inf')]
    labels = ['<50', '50-59', '60-69', '70-79', '80-89', '90-99', '100-119', '120+']
    weight_df['Weight_Group'] = pd.cut(weight_df['value_as_number'], bins=bins, labels=labels)
    results['Weight_Distribution'] = weight_df['Weight_Group'].value_counts().sort_index()

    # 身高
    height_df = df[df['unit_source_value'] == 'cm'].copy()
    bins = [1, 140, 150, 160, 170, 180, 190, float('inf')]
    labels = ['<140', '140-149', '150-159', '160-169', '170-179', '180-189', '190+']
    height_df['Height_Group'] = pd.cut(height_df['value_as_number'], bins=bins, labels=labels)
    results['Height_Distribution'] = height_df['Height_Group'].value_counts().sort_index()

    # 答案分布
    proportion_df = (
        df.groupby('observation_source_concept_id')['observation_source_value']
        .value_counts(normalize=True)
        .rename('proportion')
        .reset_index()
    )
    proportion_df['proportion'] = (proportion_df['proportion'] * 100).round(2).astype(str) + '%'
    results['Observation_Proportion'] = proportion_df

    return results
