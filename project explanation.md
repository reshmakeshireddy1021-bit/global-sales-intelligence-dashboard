# 📋 Global Sales Intelligence Dashboard — Project Explanation

<div align="center">

[![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&pause=1000&color=F2C811&width=600&lines=Project+Documentation;End-to-End+BI+Pipeline+Explained;From+Raw+Data+to+Executive+Decisions)](https://git.io/typing-svg)

</div>

<div align="center">

![Power BI](https://img.shields.io/badge/Power_BI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)
![Python](https://img.shields.io/badge/Python-3.9-blue?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-239120?style=for-the-badge&logo=plotly&logoColor=white)
![Excel](https://img.shields.io/badge/Excel-217346?style=for-the-badge&logo=microsoftexcel&logoColor=white)
![DAX](https://img.shields.io/badge/DAX-0078D4?style=for-the-badge&logo=microsoft&logoColor=white)

</div>

---

## 1️⃣ Project Overview

Many organizations store sales data in spreadsheets with no easy way to identify regional performance gaps, product profitability, or revenue anomalies. This project solves that problem by building a fully interactive **Global Sales Intelligence Dashboard** that converts **100,000+ raw transactional records** into clear, actionable business insights.

The dashboard was built end-to-end using **Python for data engineering** and **Power BI for executive visualization** — covering everything from raw data ingestion to anomaly detection to multi-format output delivery.

---

## 2️⃣ Business Problem

| Challenge | Impact |
|-----------|--------|
| Sales data scattered across spreadsheets | No unified performance view |
| No regional or segment-level visibility | Missed growth opportunities |
| Manual data preparation before every report | Hours of wasted analyst effort |
| No anomaly detection on discounts | Undetected revenue risk and discount abuse |
| Technical insights not accessible to leadership | Poor data-driven decision making |

---

## 3️⃣ Data Source

The dataset is based on the **Superstore Sales Dataset (2014–2017)** — a widely used benchmark in business intelligence that simulates real-world retail operations.

| Attribute | Details |
|-----------|---------|
| Total Orders | 5,009 customer orders |
| Time Period | 2014 to 2017 |
| Regions | West, East, Central, South |
| Segments | Consumer, Corporate, Home Office |
| Categories | Technology, Office Supplies, Furniture |
| Fields | Order date, sales, discount, profit, quantity |

A **synthetic data generation layer** was also built in Python to extend and enrich the dataset for deeper trend and anomaly analysis.

---

## 4️⃣ Tools and Technologies

| Tool | Purpose |
|------|---------|
| **Python 3.10** | Core analysis and visualization pipeline |
| **Pandas** | Data loading, cleaning, aggregation |
| **NumPy** | Statistical calculations and anomaly thresholds |
| **Matplotlib** | Static 6-panel dark-theme dashboard |
| **Seaborn** | Style enhancements |
| **Plotly** | Interactive HTML dashboard |
| **Power BI + DAX** | Executive-grade interactive dashboard |
| **OpenPyXL** | Multi-sheet Excel export for stakeholders |

---

## 5️⃣ How It Works

```
Raw Sales Data (CSV)
        │
        ▼
┌─────────────────────┐
│  Data Generation    │  — 5,009 orders with regions, categories, margins
│  & Cleaning         │
└────────┬────────────┘
         │
         ▼
┌─────────────────────┐
│  KPI Calculation    │  — Revenue, Profit, Orders, Margin %, YoY Growth
└────────┬────────────┘
         │
         ▼
┌─────────────────────┐
│  Segmented Analysis │  — Region, Segment, Category, Top 10 Products
└────────┬────────────┘
         │
         ▼
┌─────────────────────┐
│  Trend Analysis     │  — Monthly trend + 3-Month rolling average
└────────┬────────────┘
         │
         ▼
┌─────────────────────┐
│  Anomaly Detection  │  — High discount + negative profit flagging
│  (Security Layer)   │  — Statistical threshold: mean − 2σ
└────────┬────────────┘
         │
         ▼
┌─────────────────────────────────────────┐
│  Output                                 │
│  ├── Matplotlib static PNG dashboard    │
│  ├── Plotly interactive HTML            │
│  └── Excel 7-sheet stakeholder export   │
└─────────────────────────────────────────┘
```

---

## 6️⃣ Key Business Metrics

| Metric | Value |
|--------|-------|
| **Total Revenue** | $2.3 Million |
| **Total Profit** | $286,400 |
| **Total Orders** | 5,009 |
| **Profit Margin** | 12.47% |
| **Top Region** | West ($700K+) |
| **Top Segment** | Consumer ($1.16M — 52% of revenue) |
| **Top Category** | Technology ($406K) |
| **Top Product** | Canon imageCLASS ($62K) |
| **Anomalies Flagged** | 23+ high-risk transactions |
| **Data Prep Time Reduced** | 40% |

---

## 7️⃣ Key Business Insights

### 🌎 Regional Performance
The **West region leads** all territories in revenue at $700K+. The **South region** shows the lowest order volume — indicating a potential market expansion opportunity worth investigating.

### 👥 Segment Breakdown
The **Consumer segment** accounts for approximately 52% of total revenue at $1.16M — nearly double Corporate at $706K and three times Home Office at $430K. Targeted campaigns for Corporate could significantly lift overall margins.

### 📦 Category Profitability
**Technology dominates** revenue at $406K but carries higher unit risk. **Office Supplies** shows the most stable and consistent margin. **Furniture** has the lowest profit margin despite strong revenue — driven largely by aggressive discount rates.

### 📈 Trend Analysis
The **3-month moving average** reveals a gradual revenue decline in the second half of 2017 — suggesting seasonal patterns or market saturation that warrants further sub-category investigation.

### 🚨 Anomaly Detection
The statistical anomaly layer **flagged 23+ transactions** with unusually high discounts combined with negative profit — representing direct revenue risk and potential discount abuse patterns in the data.

---

## 8️⃣ Anomaly Detection — The Cybersecurity Angle

One unique aspect of this project is the **anomaly detection layer**, which applies statistical methods borrowed directly from cybersecurity threat detection:

```python
def detect_anomalies(dataframe):
    high_discount   = dataframe["Discount"] >= 0.4
    negative_profit = dataframe["Profit"] < 0
    threshold       = dataframe["Profit"].mean() - 2 * dataframe["Profit"].std()
    extreme_loss    = dataframe["Profit"] < threshold

    anomalies = dataframe[high_discount & (negative_profit | extreme_loss)].copy()
    return anomalies
```

This is the **same logic used in intrusion detection systems** — define a baseline, set a threshold, flag deviations. Applied to sales data, it surfaces transactions that may indicate:

- Unauthorized discount overrides
- Fraudulent order manipulation
- Systemic pricing errors by region or sales representative

---

## 9️⃣ Dashboard Panels

| Panel | Chart Type | Key Insight |
|-------|-----------|-------------|
| Revenue by Region | Horizontal Bar | West leads; South is weakest |
| Revenue by Category | Donut Chart | Technology dominates at 36% |
| Revenue by Segment | Bar Chart | Consumer = 52% of business |
| Monthly Trend + 3M MA | Line + Fill | Gradual H2 2017 decline visible |
| Year-over-Year Growth | Color-coded Bar | Growth peaks in 2015-2016 |
| Anomaly Detection | Scatter Plot | 23+ flagged high-risk transactions |

---

## 🔟 Skills Demonstrated

`End-to-End ETL Pipeline` · `DAX Measure Development` · `Star Schema Data Modeling` · `Executive Dashboard Design` · `Statistical Anomaly Detection` · `Data Storytelling` · `Python` · `Pandas` · `Plotly` · `Power BI` · `Multi-format Output Delivery`

---

## 🚀 Future Roadmap

- [ ] Real-time data refresh integration
- [ ] Predictive sales forecasting using Python ML models
- [ ] Customer segmentation and cohort analysis
- [ ] Publish to Power BI Service for live web sharing
- [ ] Add what-if scenario and sensitivity analysis

---

## 👤 Author

**Reshma Keshireddy** — Data Analytics & Business Intelligence

LinkedIn: https://linkedin.com/in/reshma-keshireddy-1283b91b6
GitHub: https://github.com/reshmakeshireddy1021-bit

---

> *"Data without context is just numbers. A great dashboard turns numbers into decisions."*

---

> *This project is for educational and portfolio purposes only.*
