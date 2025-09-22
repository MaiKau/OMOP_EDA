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

---

