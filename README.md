# OMOP_EDA

**OMOP_EDA** 是一個專為 **OMOP Common Data Model (CDM)** 格式設計的臨床資料探索分析套件。  
它能協助研究人員快速進行 **描述性統計、交叉分析與疾病群體比較**，模組化設計可針對不同資料表分別分析，無需一次執行所有分析。  

---

## 功能特色

- **Demographics**  
  - 年齡分布、性別比例  
  - 年齡 × 性別、種族 × 性別、族群 × 性別交叉表  

- **Observations**  
  - 體重分布 (kg)  
  - 身高分布 (cm)  
  - Observation source 觀察值比例統計  

- **Conditions**  
  - Condition × 性別  
  - Condition × 年齡群  
  - Condition × 年份  

- **Comparisons**  
  - 兩疾病年齡分布比較  
    - Shapiro-Wilk 常態性檢定  
    - Mann-Whitney U test (非參數檢定)  
  - 兩疾病性別比例比較 (卡方檢定)  

---

## 安裝方式

1. 下載專案壓縮檔 `OMOP.zip`  
2. 使用 pip 安裝：  

```bash
pip install OMOP.zip
安裝完成後即可匯入使用。

使用方法
python
複製程式碼
from OMOP import analyze_demographics, analyze_observations, analyze_conditions, compare_conditions

# 人口統計分析
demo_results = analyze_demographics(df_person)
print(demo_results['AgeGender'])

# observation 分析
obs_results = analyze_observations(df_observation, df_person)
print(obs_results['Weight_Distribution'])

# condition 分析
cond_results = analyze_conditions(df_condition, df_person)
print(cond_results['Condition_Gender'])

# 疾病比較 (例如：肺癌 vs 口腔癌)
comp_results = compare_conditions(df_condition, df_person, cond1=46718999, cond2=46718920)
print(comp_results['MannWhitneyU'])
print(comp_results['ChiSquare'])
所有分析函式皆回傳 dict，可透過指定 key 存取結果，例如：

demo_results['AgeGender'] → 年齡 × 性別交叉表

obs_results['Weight_Distribution'] → 體重分布

comp_results['MannWhitneyU'] → 兩疾病年齡分布的檢定結果

適用情境
臨床資料探索分析 (Exploratory Data Analysis, EDA)

醫療研究人員快速產生描述性統計與疾病分布比較

作為 OHDSI/Atlas 等 OMOP 工具的輔助分析

系統需求
Python 3.8+

pandas

matplotlib

scipy

