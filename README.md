# OMOP_EDA

**OMOP_EDA** is an exploratory data analysis (EDA) package designed specifically for the **OMOP Common Data Model (CDM)** format.  
It helps researchers quickly perform **descriptive statistics, cross-analyses, and disease cohort comparisons**.  
With its modular design, it allows separate analysis of different data tables without requiring all analyses to be executed at once.  

---

## Features

- **Demographics**  
  - Age distribution, gender ratio  
  - Age × Gender, Race × Gender, Ethnicity × Gender cross tables  

- **Observations**  
  - Weight distribution (kg)  
  - Height distribution (cm)  
  - Observation source value proportion statistics  

- **Conditions**  
  - Condition × Gender  
  - Condition × Age group  
  - Condition × Year  

- **Comparisons**  
  - Age distribution comparison between two diseases  
    - Shapiro-Wilk normality test  
    - Mann-Whitney U test (non-parametric test)  
  - Gender ratio comparison between two diseases (Chi-square test)  

---

## Installation

1. Download the project archive `OMOP.zip`  
2. Install using pip:  

```bash
pip install OMOP.zip
```

---

## Usage
```bash
from OMOP import analyze_demographics, analyze_observations, analyze_conditions, compare_conditions
```

**person demographic analysis**
```bash
demo_results = analyze_demographics(df_person)
print(demo_results['AgeGender'])
```

**observation analysis**
```bash
obs_results = analyze_observations(df_observation, df_person)
print(obs_results['Weight_Distribution'])
```

**condition analysis**
```bash
cond_results = analyze_conditions(df_condition, df_person)
print(cond_results['Condition_Gender'])
```

**disease comparison (e.g., Lung Cancer vs Oral Cancer)**
```bash
comp_results = compare_conditions(df_condition, df_person, cond1=46718999, cond2=46718920)
print(comp_results['MannWhitneyU'])
print(comp_results['ChiSquare'])
```

**All analysis functions return a dict. Results can be accessed by specifying the key, for example:**
```bash
demo_results['AgeGender']
obs_results['Weight_Distribution'] 
comp_results['MannWhitneyU']
```

**Check available keys in the current dict:**
```bash
demo_results.keys()
obs_results.keys()
cond_results.keys()
comp_results.keys()
```

**Use cases**  
1.Exploratory Data Analysis (EDA) for clinical data  
2.Rapid generation of descriptive statistics and disease distribution comparisons for medical researchers    
3.Supplementary analysis for OMOP tools such as OHDSI/Atlas  

**System requirements**  
Python 3.8+  
pandas 2.23+  
matplotlib 3.94+  
scipy 1.13.1+  
