import pandas as pd
from .utils import add_total_and_pct

def analyze_conditions(df_condition: pd.DataFrame, df_person: pd.DataFrame):
    results = {}
    df = pd.merge(df_condition, df_person, how='left', on='person_id')

    # Condition x Gender
    cond_gender = pd.crosstab(df['gender_source_value'], df['condition_source_concept_id'])
    results['Condition_Gender'] = add_total_and_pct(cond_gender)

    # Condition x AgeGroup
    cond_age = pd.crosstab(df['Age_Group'], df['condition_source_concept_id'])
    results['Condition_AgeGroup'] = add_total_and_pct(cond_age)

    # Condition x Year
    df['condition_start_date'] = pd.to_datetime(df['condition_start_date'], errors='coerce')
    df['condition_start_year'] = df['condition_start_date'].dt.year
    cond_year = pd.crosstab(df['condition_start_year'], df['condition_source_concept_id'])
    results['Condition_Year'] = cond_year

    return results
