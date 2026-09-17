---
type: "chatgpt-conversation"
source: "ChatGPT export"
conversation_id: "6973b366-b2fc-8320-94c1-71b76ac6c242"
created: 1769190248.210683
updated: 1769190277.269863
resource_section: true
---

# SQL and Data Concepts

## User

1. Difference between 𝗜𝗡𝗡𝗘𝗥 𝗝𝗢𝗜𝗡 and 𝗟𝗘𝗙𝗧 𝗝𝗢𝗜𝗡
2. 𝗪𝗛𝗘𝗥𝗘 𝘃𝘀 𝗛𝗔𝗩𝗜𝗡𝗚 (real use case)
3. Write SQL to find the 𝟮𝗻𝗱 𝗵𝗶𝗴𝗵𝗲𝘀𝘁 𝘀𝗮𝗹𝗮𝗿𝘆
4. How do you handle 𝗺𝗶𝘀𝘀𝗶𝗻𝗴 𝘃𝗮𝗹𝘂𝗲𝘀 in a dataset?
5. How do you detect 𝗼𝘂𝘁𝗹𝗶𝗲𝗿𝘀 (IQR / Z-score / boxplot)?
6. Explain 𝗡𝗼𝗿𝗺𝗮𝗹𝗶𝘇𝗮𝘁𝗶𝗼𝗻 (𝟭𝗡𝗙, 𝟮𝗡𝗙, 𝟯𝗡𝗙)
7. 𝗢𝗟𝗧𝗣 𝘃𝘀 𝗢𝗟𝗔𝗣 with examples
8. What is 𝗱𝗮𝘁𝗮 𝗰𝗹𝗲𝗮𝗻𝗶𝗻𝗴 and your checklist?
9. Power BI: 𝗠𝗲𝗮𝘀𝘂𝗿𝗲𝘀 𝘃𝘀 𝗖𝗼𝗹𝘂𝗺𝗻𝘀
10. DAX: What does 𝗖𝗔𝗟𝗖𝗨𝗟𝗔𝗧𝗘() do?
11. How do you make 𝗣𝗼𝘄𝗲𝗿 𝗕𝗜 𝗿𝗲𝗽𝗼𝗿𝘁𝘀 𝗳𝗮𝘀𝘁𝗲𝗿 for huge data?
12. Scenario: "Sales dropped in one region" - 𝗵𝗼𝘄 𝘄𝗶𝗹𝗹 𝘆𝗼𝘂 𝗶𝗻𝘃𝗲𝘀𝘁𝗶𝗴𝗮𝘁𝗲?
13. Explain 𝗚𝗿𝗼𝘂𝗽 𝗕𝘆 + common mistakes
14. Difference between 𝗖𝗢𝗨𝗡𝗧(*) 𝘃𝘀 𝗖𝗢𝗨𝗡𝗧(𝗰𝗼𝗹𝘂𝗺𝗻)
15. Tell me about a time you used data to drive a decision (project-based)

## Assistant

Below are **clear, exam-ready answers**, written the way a **student would present in a paper**, with **professional and structured explanations**.

---

### **1. Difference between INNER JOIN and LEFT JOIN**

**INNER JOIN** 
Returns only those records that have **matching values in both tables**.

**LEFT JOIN (LEFT OUTER JOIN)** 
Returns **all records from the left table** and the matched records from the right table. If there is no match, NULL values are returned for the right table.

**Key Difference:** 
INNER JOIN filters unmatched rows, whereas LEFT JOIN preserves all rows from the left table.

---

### **2. WHERE vs HAVING (with real use case)**

**WHERE** 
- Used to filter **rows before aggregation**
- Cannot be used with aggregate functions

**HAVING** 
- Used to filter **groups after aggregation**
- Used with aggregate functions like SUM, COUNT, AVG

**Use Case:** 
Find departments having total salary greater than 5,00,000.

```sql
SELECT department, SUM(salary)
FROM employees
GROUP BY department
HAVING SUM(salary) > 500000;
```

---

### **3. SQL to find the 2nd highest salary**

```sql
SELECT MAX(salary)
FROM employees
WHERE salary < (SELECT MAX(salary) FROM employees);
```

This query first finds the highest salary and then selects the maximum salary less than it.

---

### **4. How do you handle missing values in a dataset?**

Missing values can be handled by:
- **Removing rows** (if missing data is small and random)
- **Mean/Median/Mode imputation**
- **Forward/Backward fill** (time-series data)
- **Predictive imputation** (regression, ML models)
- **Flagging missing values** as a separate category

The method depends on business impact and data distribution.

---

### **5. How do you detect outliers?**

**IQR Method** 
- Outliers < Q1 − 1.5×IQR or > Q3 + 1.5×IQR

**Z-Score Method** 
- Outliers if Z-score > ±3

**Boxplot** 
- Visual representation to easily identify extreme values

Each method is selected based on data size and distribution.

---

### **6. Explain Normalization (1NF, 2NF, 3NF)**

**1NF (First Normal Form)** 
- Atomic values 
- No repeating groups

**2NF (Second Normal Form)** 
- In 1NF 
- No partial dependency on composite primary key

**3NF (Third Normal Form)** 
- In 2NF 
- No transitive dependency

**Purpose:** Reduce redundancy and improve data integrity.

---

### **7. OLTP vs OLAP with examples**

**OLTP (Online Transaction Processing)** 
- Day-to-day transactions 
- Fast inserts and updates 
- Example: Banking system, Order processing

**OLAP (Online Analytical Processing)** 
- Analytical queries 
- Large historical data 
- Example: Sales trend analysis, BI dashboards

---

### **8. What is data cleaning and your checklist?**

**Data Cleaning** is the process of improving data quality for analysis.

**Checklist:**
- Handle missing values
- Remove duplicates
- Fix data types
- Handle outliers
- Standardize formats
- Validate business rules

---

### **9. Power BI: Measures vs Columns**

**Calculated Columns**
- Computed row by row
- Stored in memory
- Static after refresh

**Measures**
- Calculated dynamically
- Based on filter context
- Efficient and recommended for aggregations

---

### **10. DAX: What does CALCULATE() do?**

`CALCULATE()` modifies the **filter context** of a measure.

It is the most powerful DAX function used to apply filters dynamically.

Example:
```DAX
Total Sales India = 
CALCULATE(SUM(Sales\[Amount\]), Sales\[Country\] = "India")
```

---

### **11. How do you make Power BI reports faster for huge data?**

- Use **Star Schema**
- Reduce columns and rows
- Prefer **measures over columns**
- Use **Import mode with aggregations**
- Optimize DAX
- Use **incremental refresh**
- Avoid unnecessary visuals

---

### **12. Scenario: Sales dropped in one region – how will you investigate?**

Approach:
1. Validate data freshness and accuracy
2. Compare historical trends
3. Break down by product, customer, channel
4. Check pricing, discounts, and inventory
5. Identify external factors (competition, seasonality)
6. Present findings with actionable insights

---

### **13. Explain GROUP BY + common mistakes**

**GROUP BY** is used to aggregate data based on one or more columns.

**Common Mistakes:**
- Using non-aggregated columns without GROUP BY
- Using WHERE instead of HAVING
- Incorrect granularity

---

### **14. COUNT(*) vs COUNT(column)**

**COUNT(*)**
- Counts all rows (including NULLs)

**COUNT(column)**
- Counts only non-NULL values

---

### **15. Tell me about a time you used data to drive a decision**

In one project, I analyzed sales data to identify declining performance in a product category. After cleaning and segmenting the data, I found that price increases caused reduced demand in one region. Based on this insight, a pricing adjustment was recommended, which improved sales volume in the following quarter.

---

If you want, I can also:
- Convert this into **interview answers**
- Provide **one-line crisp responses**
- Add **SQL + Power BI mini case questions**

Just tell me.

## Resources

No structured attachments or external references were present in this conversation.
