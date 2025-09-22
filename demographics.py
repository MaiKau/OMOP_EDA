import pandas as pd
from datetime import datetime
from .utils import add_total_and_pct

def analyze_demographics(df_person: pd.DataFrame):
    results = {}
    current_year = datetime.now().year
    df_person = df_person.copy()
    df_person['birth_datetime'] = pd.to_datetime(df_person['birth_datetime'], errors='coerce')
    df_person['Current_Age'] = current_year - df_person['birth_datetime'].dt.year

    bins = [-1, 17, 29, 39, 49, 59, 69, 79, 89, float('inf')]
    labels = ['<18', '18-29', '30-39', '40-49', '50-59', '60-69', '70-79', '80-89', '89+']
    df_person['Age_Group'] = pd.cut(df_person['Current_Age'], bins=bins, labels=labels)

    age_gender = pd.crosstab(df_person['Age_Group'], df_person['gender_source_value'])
    results['AgeGender'] = add_total_and_pct(age_gender)

    race_gender = pd.crosstab(df_person['race_source_value'], df_person['gender_source_value'])
    results['RaceGender'] = add_total_and_pct(race_gender)

    ethnicity_gender = pd.crosstab(df_person['ethnicity_source_value'], df_person['gender_source_value'])
    results['EthnicityGender'] = add_total_and_pct(ethnicity_gender)

    return results
