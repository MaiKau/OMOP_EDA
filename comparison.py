import pandas as pd
from scipy.stats import shapiro, mannwhitneyu, chi2_contingency

def compare_conditions(df_condition: pd.DataFrame, df_person: pd.DataFrame, cond1: int, cond2: int):
    results = {}
    df = pd.merge(df_condition, df_person, how='left', on='person_id')

    group1 = df[df['condition_type_concept_id'] == cond1]['Current_Age']
    group2 = df[df['condition_type_concept_id'] == cond2]['Current_Age']

    desc = pd.DataFrame({
        str(cond1): group1.describe(),
        str(cond2): group2.describe()
    })
    results['Descriptive'] = desc

    results['Shapiro'] = {
        str(cond1): shapiro(group1),
        str(cond2): shapiro(group2)
    }

    u_stat, p_value = mannwhitneyu(group1, group2, alternative='two-sided')
    results['MannWhitneyU'] = {'U': u_stat, 'p': p_value}

    median_values = df.groupby('condition_type_concept_id')['Current_Age'].median()
    results['Median'] = median_values

    contingency_table = pd.crosstab(df['condition_type_concept_id'], df['gender_source_value'])
    chi2, p, dof, expected = chi2_contingency(contingency_table)
    results['ChiSquare'] = {'Chi2': chi2, 'p': p, 'table': contingency_table}

    return results
