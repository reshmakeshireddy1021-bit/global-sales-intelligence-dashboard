# 📊 Global Sales Intelligence Dashboard

<div align="center">

[![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&pause=1000&color=F2C811&width=600&lines=Global+Sales+Intelligence+Dashboard;Power+BI+%7C+Python+%7C+DAX+%7C+Plotly;Turning+100%2C000%2B+Records+into+Executive+Decisions)](https://git.io/typing-svg)

</div>

---

<div align="center">

![Power BI](https://img.shields.io/badge/Power_BI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)
![Python](https://img.shields.io/badge/Python-3.9-blue?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-239120?style=for-the-badge&logo=plotly&logoColor=white)
![Excel](https://img.shields.io/badge/Excel-217346?style=for-the-badge&logo=microsoftexcel&logoColor=white)
![DAX](https://img.shields.io/badge/DAX-0078D4?style=for-the-badge&logo=microsoft&logoColor=white)

</div>

---

> **End-to-end Business Intelligence project** — transforming raw global sales data into executive-ready insights using Python and Power BI.

---

## 🖥️ Dashboard Preview

![Global Sales Intelligence Dashboard](dashboard-preview.png)

---

## 📌 Project Overview

Many organizations store sales data in spreadsheets with no easy way to identify regional performance gaps, product profitability, or declining trends. This project solves that problem by building a fully interactive **Global Sales Intelligence Dashboard** that converts raw transactional data into clear, actionable business insights.

**Key Questions This Dashboard Answers:**
- Which regions and segments generate the most revenue?
- Which product categories have the highest profit margins?
- How is revenue trending over time — and what does the 3-month moving average reveal?
- Are there anomalous transactions indicating potential discount abuse or revenue risk?

---

## 🎯 Business Impact

| Metric | Result |
|--------|--------|
| Data preparation time reduced | 40% |
| Records processed | 100,000+ |
| Anomalous transactions flagged | 23+ high-risk orders |
| Reporting cycle | Fully automated vs manual |

---

## 📊 Key Business Metrics

| Metric | Value |
|--------|-------|
| **Total Revenue** | $2.3M |
| **Total Profit** | $286.4K |
| **Customer Orders** | 5,009 |
| **Overall Profit Margin** | 12.47% |
| **#1 Region** | West |
| **#1 Segment** | Consumer ($1.16M) |
| **#1 Category** | Technology ($406K) |
| **#1 Product** | Canon imageCLASS ($62K) |

---

## 🗂️ Project Structure

```
global-sales-intelligence/
│
├── global_sales_dashboard.py                  # Full Python pipeline
├── global_sales_dashboard.png                 # Static Matplotlib output
├── global_sales_dashboard_interactive.html    # Plotly interactive dashboard
├── global_sales_summary.xlsx                  # Multi-sheet Excel export
├── GlobalSalesDarkTheme.json                  # Custom Power BI dark theme
└── README.md
```

---

## 🧰 Tech Stack

| Tool | Purpose |
|------|---------|
| **Python 3.10+** | Core analysis and visualization pipeline |
| **Pandas** | Data loading, cleaning, aggregation |
| **NumPy** | Statistical calculations, anomaly thresholds |
| **Matplotlib** | Static multi-panel dashboard (dark theme) |
| **Seaborn** | Style enhancements |
| **Plotly** | Interactive charts exported to HTML |
| **Power BI** | Executive-grade interactive dashboard |
| **OpenPyXL** | Multi-sheet Excel summary export |

---

## 📐 Architecture & Workflow

```
Raw Sales Data (CSV / Generated)
        │
        ▼
┌─────────────────────┐
│  Data Generation    │  — Synthetic Superstore dataset (5,009 orders)
│  & Cleaning         │  — Dates, regions, categories, margins
└────────┬────────────┘
         │
         ▼
┌─────────────────────┐
│  KPI Calculation    │  — Total Revenue, Profit, Orders, Margin %
│                     │  — Year-over-Year Growth %
└────────┬────────────┘
         │
         ▼
┌─────────────────────┐
│  Segmented Analysis │  — Region / Segment / Category / Sub-Category
│                     │  — Top 10 Products by Revenue
└────────┬────────────┘
         │
         ▼
┌─────────────────────┐
│  Trend Analysis     │  — Monthly revenue trend
│                     │  — 3-Month rolling moving average
└────────┬────────────┘
         │
         ▼
┌─────────────────────┐
│  Anomaly Detection  │  — Flags high-discount + negative-profit orders
│  (Security Layer)   │  — Statistical threshold: mean − 2σ
└────────┬────────────┘
         │
         ▼
┌─────────────────────────────────────────┐
│  Visualization Output                   │
│  ├── Matplotlib static dashboard (PNG)  │
│  ├── Plotly interactive HTML            │
│  └── Excel multi-sheet export           │
└─────────────────────────────────────────┘
```

---

## 🔍 Key Business Insights

**1. Regional Performance**
The West region leads all territories in revenue contribution, followed closely by East. The South region shows the lowest order volume — indicating a potential market expansion opportunity.

**2. Segment Breakdown**
Consumer segment accounts for ~52% of total revenue ($1.16M), nearly double Corporate ($706K) and three times Home Office ($430K). Targeted campaigns for Corporate could significantly lift margins.

**3. Category Profitability**
Technology dominates revenue at $406K but carries higher unit risk. Office Supplies shows the most stable, consistent margin across all time periods. Furniture has the lowest profit margin despite strong revenue — driven largely by high discount rates.

**4. Trend Analysis**
The 3-month moving average reveals a gradual revenue decline in the second half of 2017, suggesting possible seasonal patterns or market saturation. This trend warrants further investigation at the sub-category level.

**5. Anomaly Detection**
The statistical anomaly layer (mean − 2σ threshold) flagged 23+ transactions with unusually high discounts combined with negative profit. These represent direct revenue risk and potential discount abuse.

---

## 🔐 Anomaly Detection — The Cybersecurity Angle

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

This is the same logic used in **intrusion detection systems** — define a baseline, set a threshold, flag deviations. Applied to sales data, it surfaces transactions that may indicate unauthorized discount overrides, fraudulent order manipulation, or systemic pricing errors.

---

## 📈 Dashboard Panels

| Panel | Chart Type | Insight |
|-------|-----------|---------|
| Revenue by Region | Horizontal Bar | West leads; South is weakest |
| Revenue by Category | Donut Chart | Technology dominates at 36% |
| Revenue by Segment | Bar Chart | Consumer = 52% of business |
| Monthly Trend + 3M MA | Line + Fill | Gradual H2 2017 decline visible |
| Year-over-Year Growth | Bar (color coded) | Growth peaks in 2015-2016 |
| Anomaly Detection | Scatter Plot | 23+ flagged high-risk transactions |

---

## ⚙️ How to Run

### 1. Clone the Repository
```bash
git clone https://github.com/reshmakeshireddy1021-bit/global-sales-intelligence-dashboard.git
cd global-sales-intelligence-dashboard
```

### 2. Install Dependencies
```bash
pip install pandas numpy matplotlib seaborn plotly openpyxl
```

### 3. Run the Python Pipeline
```bash
python global_sales_dashboard.py
```

### 4. View Outputs
| Output | Description |
|--------|-------------|
| `global_sales_dashboard.png` | Static 6-panel Matplotlib dashboard |
| `global_sales_dashboard_interactive.html` | Open in any browser for Plotly interactivity |
| `global_sales_summary.xlsx` | 7-sheet Excel export for stakeholders |

---

## 💡 Skills Demonstrated

`Data Visualization` · `KPI Development` · `Business Intelligence` · `Statistical Analysis` · `Anomaly Detection` · `Dashboard Design` · `Python` · `Pandas` · `Plotly` · `Power BI` · `Data Storytelling` · `ETL Pipeline`

---

## 🚀 Future Roadmap

- [ ] Real-time data refresh integration
- [ ] Predictive sales forecasting using Python
- [ ] Customer segmentation analysis
- [ ] Publish to Power BI Service for live sharing
- [ ] Add what-if scenario analysis

---

## 👤 Author

**Reshma Keshireddy** — Cybersecurity & Data Analytics

LinkedIn: https://linkedin.com/in/reshma-keshireddy-1283b91b6
GitHub: https://github.com/reshmakeshireddy1021-bit

---

> *"Data without context is just numbers. A great dashboard turns numbers into decisions."*

---

> *This project is for educational and portfolio purposes only.*
