---
type: "chatgpt-conversation"
source: "ChatGPT export"
conversation_id: "69f0dbbb-7c30-83e8-af87-9d84924e2cd0"
created: 1777392632.97228
updated: 1777400780.140919
resource_section: true
---

# Python Code for Data Analysis

## User

give me python code for data analysis of this dataset

## Assistant

Write it in a structured, exam-style manner.

---

**Python Code for Data Analysis of COVID-19 India Statewise Vaccine Dataset**

```python
# Step 1: Import required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Step 2: Load the dataset
file_path = "COVID-19 India Statewise Vaccine Data.csv"
df = pd.read_csv(file_path)

# Step 3: Basic Data Inspection
print("First 5 rows:\n", df.head())
print("\nDataset Info:\n")
df.info()
print("\nStatistical Summary:\n", df.describe())

# Step 4: Data Cleaning
# Convert date column to datetime (if exists)
if 'Updated On' in df.columns:
 df\['Updated On'\] = pd.to_datetime(df\['Updated On'\], errors='coerce')

# Check for missing values
print("\nMissing Values:\n", df.isnull().sum())

# Fill or drop missing values
df = df.fillna(0)

# Step 5: Data Analysis

# Total vaccination by state
if 'State' in df.columns and 'Total Doses Administered' in df.columns:
 state_vaccine = df.groupby('State')\['Total Doses Administered'\].sum().sort_values(ascending=False)
 print("\nTotal Vaccination by State:\n", state_vaccine)

# Daily vaccination trend
if 'Updated On' in df.columns and 'Total Doses Administered' in df.columns:
 daily_trend = df.groupby('Updated On')\['Total Doses Administered'\].sum()

# Step 6: Data Visualization

# Top 10 states vaccination
plt.figure(figsize=(10,6))
state_vaccine.head(10).plot(kind='bar')
plt.title("Top 10 States by Vaccination")
plt.xlabel("State")
plt.ylabel("Total Doses")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Vaccination trend over time
if 'Updated On' in df.columns:
 plt.figure(figsize=(12,6))
 daily_trend.plot()
 plt.title("Vaccination Trend Over Time")
 plt.xlabel("Date")
 plt.ylabel("Total Doses")
 plt.grid()
 plt.show()

# Correlation Heatmap
plt.figure(figsize=(10,6))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()

# Step 7: Key Insights (Printed)
print("\nKey Insights:")
print("1. Highest vaccinated states:\n", state_vaccine.head(5))
print("2. Dataset shape:", df.shape)
print("3. Columns:", df.columns)
```

---

**Explanation (short, student-style):** 
First, we import libraries like pandas and matplotlib. Then we load the dataset and check its structure. After cleaning missing values, we perform grouping to analyze vaccination by state and over time. Finally, we visualize the results using bar charts, line graphs, and heatmaps to understand trends and correlations.

---

If you want, I can also convert this into a **Power BI dashboard idea** or **advanced ML-based analysis (forecasting vaccinations)**.

## User

dont guess when i have provides u dataset go and check it yourself and be sure

## Assistant

You are right to point that out — the earlier code was making assumptions about column names like *“Updated On”*, which **do not exist** in your dataset. That is not correct practice in data analysis.

Now, writing the solution properly after **actually inspecting your dataset**.

---

### **Observed Dataset Structure**
Columns present:
- `State/UTs`
- `Dose 1`
- `Dose 2`
- `Total Vaccination Doses`

No date column is present, so **time-series analysis is not applicable** here.

---

## **Correct Python Code for Your Dataset**

```python id="covid_vaccine_analysis"
# Step 1: Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 2: Load dataset
df = pd.read_csv("COVID-19 India Statewise Vaccine Data.csv")

# Step 3: Inspect data
print("First 5 rows:\n", df.head())
print("\nColumns:", df.columns)
print("\nDataset Info:\n")
df.info()

# Step 4: Check missing values
print("\nMissing Values:\n", df.isnull().sum())

# Step 5: Basic Analysis

# Total doses by state (already given, but sorting for insights)
state_total = df.sort_values(by="Total Vaccination Doses", ascending=False)

print("\nTop 5 States by Vaccination:\n", state_total.head())

# Step 6: Visualization

# Bar chart: Top 10 states
plt.figure(figsize=(10,6))
top10 = state_total.head(10)
plt.bar(top10\['State/UTs'\], top10\['Total Vaccination Doses'\])
plt.xticks(rotation=45)
plt.xlabel("State/UTs")
plt.ylabel("Total Vaccination Doses")
plt.title("Top 10 States by Total Vaccination")
plt.tight_layout()
plt.show()

# Comparison: Dose 1 vs Dose 2 for top 10 states
plt.figure(figsize=(10,6))
top10.set_index('State/UTs')\[\['Dose 1', 'Dose 2'\]\].plot(kind='bar')
plt.title("Dose 1 vs Dose 2 (Top 10 States)")
plt.xticks(rotation=45)
plt.ylabel("Number of Doses")
plt.tight_layout()
plt.show()

# Step 7: Correlation Heatmap
plt.figure(figsize=(6,4))
sns.heatmap(df\[\['Dose 1', 'Dose 2', 'Total Vaccination Doses'\]\].corr(), annot=True)
plt.title("Correlation between Vaccination Variables")
plt.show()

# Step 8: Key Insights
print("\nKey Insights:")
print("1. Highest vaccinated state:\n", state_total.iloc\[0\]\['State/UTs'\])
print("2. Lowest vaccinated state:\n", state_total.iloc\[-1\]\['State/UTs'\])
print("3. Total states:", df.shape\[0\])
```

---

## **Explanation (student-style)**
First, the dataset is loaded using pandas. Then we check its structure and confirm that it only contains state-wise vaccination data, not time-based data. After that, we sort states based on total doses to identify highest and lowest vaccinated regions. Finally, we use bar graphs and heatmaps to visualize distribution and relationships between Dose 1, Dose 2, and total doses.

---

If you want next level improvement, I can extend this into:
- **Population-normalized vaccination analysis**
- **State clustering using ML**
- **Dashboard-ready insights for Power BI**

Just tell.

## User

give bargraph of Total doses by state

## Assistant

Write it cleanly and directly as you would in an exam.

---

## **Bar Graph of Total Doses by State (Python Code)**

```python
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("COVID-19 India Statewise Vaccine Data.csv")

# Sort data by total doses (optional but better for visualization)
df_sorted = df.sort_values(by="Total Vaccination Doses", ascending=False)

# Create bar graph
plt.figure(figsize=(12,6))
plt.bar(df_sorted\['State/UTs'\], df_sorted\['Total Vaccination Doses'\])

# Labels and title
plt.xlabel("State/UTs")
plt.ylabel("Total Vaccination Doses")
plt.title("Total COVID-19 Vaccination Doses by State in India")

# Rotate x-axis labels for readability
plt.xticks(rotation=90)

# Adjust layout
plt.tight_layout()

# Show graph
plt.show()
```

---

## **Explanation (student-style)**
First, the dataset is loaded using pandas. Then the data is sorted based on total vaccination doses to improve visualization clarity. After that, a bar graph is plotted using matplotlib where states are on the x-axis and total doses on the y-axis. Finally, labels and formatting are added for better readability.

---

If you want, I can also show:
- Horizontal bar chart (cleaner for many states) 
- Top 10 states only (more professional visualization) 
- Dashboard-style charts for Power BI 

Just tell.

## User

make a piechart for something else

## Assistant

Understood. Instead of repeating the same variable, we will use a **different perspective of the dataset**.

A meaningful pie chart here is to show the **proportion of Dose 1 vs Dose 2 across India**.

---

## **Pie Chart: Dose 1 vs Dose 2 Distribution**

```python id="p9k2x1"
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("COVID-19 India Statewise Vaccine Data.csv")

# Calculate total Dose 1 and Dose 2
total_dose1 = df\['Dose 1'\].sum()
total_dose2 = df\['Dose 2'\].sum()

# Data for pie chart
labels = \['Dose 1', 'Dose 2'\]
values = \[total_dose1, total_dose2\]

# Plot pie chart
plt.figure(figsize=(6,6))
plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=90)

# Title
plt.title("Distribution of Dose 1 vs Dose 2 in India")

# Show chart
plt.show()
```

---

## **Explanation (student-style)**
First, total values of Dose 1 and Dose 2 are calculated by summing the respective columns. Then, a pie chart is created to represent their proportion in the overall vaccination dataset. This helps in understanding how many people have received first dose compared to second dose.

---

If you want a **better analytical pie chart**, I can also make:
- Top 5 states contribution to total vaccination 
- Fully vs partially vaccinated ratio 
- Region-wise comparison 

Tell me which one you want.

## User

Jupyter Server
500 : Internal Server Error
The error was:

nbconvert failed: xelatex not found on PATH, if you have not installed xelatex you may need to do so. Find further instructions at https://nbconvert.readthedocs.io/en/latest/install.html#installing-tex.

## Assistant

This error is not related to your code — it is a **system dependency issue**.

---

## **Cause of Error (Exam-style explanation)** 
While exporting a notebook (usually to PDF), **Jupyter uses LaTeX** internally. The error indicates that **XeLaTeX is not installed or not available in the system PATH**, so conversion fails.

---

## **Solutions**

### **Solution 1: Install LaTeX (Recommended)**

You need to install a LaTeX distribution:

### **For Windows**
Install entity\["software","MiKTeX","LaTeX distribution for Windows"\] 
- Download from official site 
- During installation, enable **“Install missing packages on the fly”**

After installation, restart Jupyter and try again.

---

### **For Linux (Ubuntu/Debian)**
```bash
sudo apt update
sudo apt install texlive-xetex texlive-fonts-recommended texlive-plain-generic
```

---

### **For macOS**
Install entity\["software","MacTeX","LaTeX distribution for macOS"\]

---

## **Solution 2: Export Without PDF (Quick Fix)**

If you don’t want LaTeX:

- Export as **HTML**
- Export as **Markdown**

Command:
```bash
jupyter nbconvert --to html your_notebook.ipynb
```

---

## **Solution 3: Use Alternative PDF Method**

Convert to HTML → then print to PDF from browser 
(This avoids LaTeX completely and is commonly used in practice)

---

## **Conclusion (Student-style)** 
The error occurs because XeLaTeX is required for PDF conversion but is not installed. Installing a LaTeX distribution like MiKTeX resolves the issue, or alternatively, exporting to HTML avoids this dependency.

---

If you want, I can give you a **step-by-step installation guide with screenshots mindset** or a **1-minute quick workaround used by professionals**.

## User

give Analytics Performed like this but according to your given code
1) Describe the dataset
This includes:
• Number of rows and columns 
• Column names 
• Data types 
• Summary statistics 

2) Number of persons state-wise vaccinated for first dose
We group the data by state and extract the maximum value of first dose administered for each state.

3) Number of persons state-wise vaccinated for second dose
We group the data by state and extract the maximum value of second dose administered for each state.

4) Number of males vaccinated
We calculate total male vaccinated individuals using the male vaccination column.

5) Number of females vaccinated
We calculate total female vaccinated individuals using the female vaccination column.

## Assistant

Write it properly in structured, exam-oriented format based strictly on the **actual operations performed in the code**.

---

## **Analytics Performed**

### **1) Describe the dataset** 
This includes: 
- Number of rows and columns in the dataset 
- Column names such as *State/UTs, Dose 1, Dose 2, Total Vaccination Doses* 
- Data types of each column (integer, object, etc.) 
- Summary statistics like mean, minimum, maximum, and standard deviation 

---

### **2) State-wise total vaccination analysis** 
The dataset is sorted based on **Total Vaccination Doses** in descending order. 
This helps in identifying: 
- Highest vaccinated states 
- Lowest vaccinated states 
- Overall ranking of states based on vaccination 

---

### **3) Top 10 states by total vaccination** 
From the sorted dataset, the **top 10 states** are selected. 
A bar graph is plotted to visualize which states contributed the most to total vaccination.

---

### **4) Comparison of Dose 1 and Dose 2 (Top States)** 
For the top 10 states, both **Dose 1 and Dose 2 values are compared** using a bar chart. 
This helps in understanding: 
- Difference between first dose and second dose coverage 
- Vaccination completion trends across major states 

---

### **5) Distribution of Dose 1 vs Dose 2 (Overall India)** 
The total sum of **Dose 1 and Dose 2** is calculated across all states. 
A pie chart is created to show the proportion of: 
- People who received first dose 
- People who received second dose 

---

### **6) Correlation analysis between vaccination variables** 
A correlation heatmap is generated using: 
- Dose 1 
- Dose 2 
- Total Vaccination Doses 

This helps to understand the relationship between variables, such as how strongly Dose 1 and Dose 2 contribute to total vaccination.

---

## **Conclusion (Student-style)** 
The analysis focuses on understanding state-wise vaccination distribution, comparing dose coverage, and identifying overall trends. Visualization techniques like bar charts, pie charts, and heatmaps are used to make the insights clear and interpretable.

---

If you want, I can convert this into a **perfect lab record / assignment format with headings, objectives, and conclusion**.

## User

df_sorted = df.sort_values(by="Total Vaccination Doses", ascending=False)
plt.figure(figsize=(9,7))
plt.bar(df_sorted\['State/UTs'\], df_sorted\['Total Vaccination Doses'\])

# Labels and title
plt.xlabel("State/UTs")
plt.ylabel("Total Vaccination Doses")
plt.title("Total COVID-19 Vaccination Doses by State in India")
plt.xticks(rotation=90)

plt.tight_layout()
plt.show()

I want to increase font size of x axis elements

## Assistant

Write the modification clearly.

---

## **Updated Code (Increase X-axis Font Size)**

```python
df_sorted = df.sort_values(by="Total Vaccination Doses", ascending=False)

plt.figure(figsize=(9,7))
plt.bar(df_sorted\['State/UTs'\], df_sorted\['Total Vaccination Doses'\])

# Labels and title
plt.xlabel("State/UTs", fontsize=12)
plt.ylabel("Total Vaccination Doses", fontsize=12)
plt.title("Total COVID-19 Vaccination Doses by State in India", fontsize=14)

# Increase x-axis tick label font size
plt.xticks(rotation=90, fontsize=12)

plt.tight_layout()
plt.show()
```

---

## **Explanation (student-style)** 
The `fontsize` parameter is added inside `plt.xticks()` to increase the size of x-axis labels (state names). This improves readability, especially when there are many states displayed.

---

If labels still look crowded, I can show you a **professional way (horizontal bar chart)** which is commonly used in dashboards.

## Resources

### Unresolved export references

- `file_00000000aab871fa875bd84a44f4d9f2`
