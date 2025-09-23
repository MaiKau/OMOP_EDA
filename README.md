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

## 使用方法
```bash
from OMOP import analyze_demographics, analyze_observations, analyze_conditions, compare_conditions
```

**person 人口統計分析**
```bash
demo_results = analyze_demographics(df_person)
print(demo_results['AgeGender'])
```

**observation 分析**
```bash
obs_results = analyze_observations(df_observation, df_person)
print(obs_results['Weight_Distribution'])
```

**condition 分析**
```bash
cond_results = analyze_conditions(df_condition, df_person)
print(cond_results['Condition_Gender'])
```

**疾病比較 (例如：肺癌 vs 口腔癌)**
```bash
comp_results = compare_conditions(df_condition, df_person, cond1=46718999, cond2=46718920)
print(comp_results['MannWhitneyU'])
print(comp_results['ChiSquare'])
```

**所有分析函式皆回傳 dict，可透過指定 key 存取結果，例如：**
```bash
demo_results['AgeGender']
obs_results['Weight_Distribution'] 
comp_results['MannWhitneyU']
```

**查詢當前dict產生項目：**
```bash
demo_results.keys()
obs_results.keys()
cond_results.keys()
comp_results.keys()
```

**適用情境**  
1.臨床資料探索分析 (Exploratory Data Analysis, EDA)  
2.醫療研究人員快速產生描述性統計與疾病分布比較  
3.作為 OHDSI/Atlas 等 OMOP 工具的輔助分析  

**系統需求**  
Python 3.8+  
pandas 2.23+  
matplotlib 3.94+  
scipy 1.13.1+  

