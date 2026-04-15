# =============================================================================
# Global Sales Intelligence Dashboard
# Author: Reshma Keshireddy
# Tools: Python (Pandas, Plotly, Matplotlib, Seaborn)
# Dataset: Global Superstore Sales Data (2014-2017)
# =============================================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import warnings
warnings.filterwarnings("ignore")

# =============================================================================
# SECTION 1: DATA GENERATION (Simulates the Global Superstore Dataset)
# =============================================================================

np.random.seed(42)

def generate_sales_data(n=5009):
    """
    Generates a synthetic Global Sales dataset replicating the
    structure of the Superstore dataset used in the Power BI dashboard.
    """
    regions      = ["West", "East", "Central", "South"]
    segments     = ["Consumer", "Corporate", "Home Office"]
    categories   = ["Technology", "Furniture", "Office Supplies"]
    sub_cats     = {
        "Technology":      ["Phones", "Machines", "Accessories", "Copiers"],
        "Furniture":       ["Chairs", "Tables", "Bookcases", "Furnishings"],
        "Office Supplies": ["Binders", "Paper", "Storage", "Art"]
    }
    products = {
        "Phones":       ["Canon imageCLASS", "Fellowes PB500", "Cisco TelePresence"],
        "Machines":     ["Brother HL-2240", "Hewlett Packard", "Lexmark MX611"],
        "Accessories":  ["Logitech G700s", "Plantronics CS510", "Kensington Lock"],
        "Copiers":      ["HP DesignJet", "Canon PC1060", "Xerox 1952"],
        "Chairs":       ["Global Troy", "HON 5400", "Novimex Chair"],
        "Tables":       ["Bretford CR4500", "Bevis Steel", "Chromcraft Marble"],
        "Bookcases":    ["Bush Salinas", "O'Sullivan Plantations", "Sauder Classic"],
        "Furnishings":  ["Eldon Expressions", "Fiskars 8", "Ultra Commercial"],
        "Binders":      ["Cardinal Slant-D", "Avery Non-Stick", "GBC DocuBind"],
        "Paper":        ["Hammermill Copy", "Xerox 1916", "Southworth 25%"],
        "Storage":      ["Carina Round", "Storex Durable", "Rogers Hangers"],
        "Art":          ["Sanford Pencils", "SAFCO Steel", "Acme Staple"]
    }

    dates = pd.date_range("2014-01-01", "2017-12-31", periods=n)
    region_list   = np.random.choice(regions,   n, p=[0.32, 0.29, 0.22, 0.17])
    segment_list  = np.random.choice(segments,  n, p=[0.52, 0.30, 0.18])
    category_list = np.random.choice(categories, n, p=[0.36, 0.32, 0.32])

    sub_category_list, product_list = [], []
    for cat in category_list:
        sc = np.random.choice(sub_cats[cat])
        sub_category_list.append(sc)
        product_list.append(np.random.choice(products[sc]))

    # Revenue and profit generation with realistic category margins
    base_sales = np.random.lognormal(mean=5.2, sigma=1.1, size=n)
    category_multipliers = {"Technology": 1.8, "Furniture": 1.3, "Office Supplies": 0.9}
    sales = np.array([base_sales[i] * category_multipliers[c]
                      for i, c in enumerate(category_list)])

    discount = np.random.choice([0, 0.1, 0.2, 0.3, 0.4, 0.5],
                                 n, p=[0.4, 0.25, 0.2, 0.08, 0.05, 0.02])
    margin_rates = {"Technology": 0.18, "Furniture": 0.09, "Office Supplies": 0.14}
    profit = np.array([sales[i] * (margin_rates[c] - discount[i] * 0.6)
                       for i, c in enumerate(category_list)])

    df = pd.DataFrame({
        "Order Date":    dates,
        "Region":        region_list,
        "Segment":       segment_list,
        "Category":      category_list,
        "Sub-Category":  sub_category_list,
        "Product Name":  product_list,
        "Sales":         np.round(sales, 2),
        "Profit":        np.round(profit, 2),
        "Discount":      discount,
        "Quantity":      np.random.randint(1, 15, size=n),
    })
    df["Year"]  = df["Order Date"].dt.year
    df["Month"] = df["Order Date"].dt.to_period("M").astype(str)
    return df


df = generate_sales_data()


# =============================================================================
# SECTION 2: KPI CALCULATIONS
# =============================================================================

total_sales        = df["Sales"].sum()
total_profit       = df["Profit"].sum()
total_orders       = len(df)
profit_margin_pct  = (total_profit / total_sales) * 100

print("=" * 55)
print("   GLOBAL SALES INTELLIGENCE — KEY METRICS")
print("=" * 55)
print(f"  Total Revenue          : ${total_sales:>12,.2f}")
print(f"  Total Profit           : ${total_profit:>12,.2f}")
print(f"  Customer Orders        : {total_orders:>13,}")
print(f"  Overall Profit Margin  : {profit_margin_pct:>12.2f}%")
print("=" * 55)


# =============================================================================
# SECTION 3: SEGMENT ANALYSIS
# =============================================================================

segment_summary = (
    df.groupby("Segment")
    .agg(Revenue=("Sales", "sum"), Profit=("Profit", "sum"), Orders=("Sales", "count"))
    .reset_index()
    .sort_values("Revenue", ascending=False)
)
segment_summary["Margin %"] = (segment_summary["Profit"] / segment_summary["Revenue"] * 100).round(2)

print("\n📊 Revenue by Customer Segment")
print(segment_summary.to_string(index=False))


# =============================================================================
# SECTION 4: CATEGORY & SUB-CATEGORY ANALYSIS
# =============================================================================

category_summary = (
    df.groupby("Category")
    .agg(Revenue=("Sales", "sum"), Profit=("Profit", "sum"))
    .reset_index()
    .sort_values("Revenue", ascending=False)
)
category_summary["Margin %"] = (
    category_summary["Profit"] / category_summary["Revenue"] * 100
).round(2)

print("\n📦 Revenue by Product Category")
print(category_summary.to_string(index=False))

subcategory_summary = (
    df.groupby(["Category", "Sub-Category"])
    .agg(Revenue=("Sales", "sum"), Profit=("Profit", "sum"))
    .reset_index()
    .sort_values("Revenue", ascending=False)
)

print("\n🔍 Top 5 Sub-Categories by Revenue")
print(subcategory_summary.head(5).to_string(index=False))


# =============================================================================
# SECTION 5: REGIONAL ANALYSIS
# =============================================================================

regional_summary = (
    df.groupby("Region")
    .agg(Revenue=("Sales", "sum"), Profit=("Profit", "sum"), Orders=("Sales", "count"))
    .reset_index()
    .sort_values("Revenue", ascending=False)
)
regional_summary["Margin %"] = (
    regional_summary["Profit"] / regional_summary["Revenue"] * 100
).round(2)

print("\n🌍 Revenue by Region")
print(regional_summary.to_string(index=False))


# =============================================================================
# SECTION 6: TOP PERFORMING PRODUCTS
# =============================================================================

top_products = (
    df.groupby("Product Name")
    .agg(Revenue=("Sales", "sum"), Profit=("Profit", "sum"), Orders=("Sales", "count"))
    .reset_index()
    .sort_values("Revenue", ascending=False)
    .head(10)
)
top_products["Margin %"] = (top_products["Profit"] / top_products["Revenue"] * 100).round(2)

print("\n🏆 Top 10 Products by Revenue")
print(top_products.to_string(index=False))


# =============================================================================
# SECTION 7: REVENUE TREND OVER TIME
# =============================================================================

monthly_trend = (
    df.groupby("Month")
    .agg(Revenue=("Sales", "sum"), Profit=("Profit", "sum"))
    .reset_index()
)
monthly_trend["Moving_Avg_3M"] = monthly_trend["Revenue"].rolling(window=3).mean()

print("\n📈 Monthly Revenue Trend (first 6 rows)")
print(monthly_trend.head(6).to_string(index=False))


# =============================================================================
# SECTION 8: YEAR-OVER-YEAR GROWTH
# =============================================================================

yoy = (
    df.groupby("Year")["Sales"]
    .sum()
    .reset_index()
    .rename(columns={"Sales": "Revenue"})
)
yoy["YoY Growth %"] = yoy["Revenue"].pct_change() * 100

print("\n📅 Year-over-Year Revenue Growth")
print(yoy.to_string(index=False))


# =============================================================================
# SECTION 9: ANOMALY DETECTION (Cybersecurity Angle)
# Flags transactions with unusually high discounts causing profit loss —
# a technique directly borrowed from security anomaly detection.
# =============================================================================

def detect_anomalies(dataframe):
    """
    Identifies suspicious transactions:
    - High discount (>= 40%) AND negative profit
    - Loss exceeding 2 standard deviations below mean
    """
    high_discount   = dataframe["Discount"] >= 0.4
    negative_profit = dataframe["Profit"] < 0
    threshold       = dataframe["Profit"].mean() - 2 * dataframe["Profit"].std()
    extreme_loss    = dataframe["Profit"] < threshold

    anomalies = dataframe[high_discount & (negative_profit | extreme_loss)].copy()
    anomalies["Anomaly Reason"] = np.where(
        anomalies["Profit"] < threshold,
        "Extreme Loss (>2σ below mean)",
        "High Discount + Negative Profit"
    )
    return anomalies

anomalies = detect_anomalies(df)
print(f"\n🔐 Anomaly Detection — Flagged Transactions: {len(anomalies)}")
print(f"   Estimated Revenue at Risk: ${abs(anomalies['Profit'].sum()):,.2f}")
if not anomalies.empty:
    print(anomalies[["Order Date", "Region", "Category", "Sales",
                      "Profit", "Discount", "Anomaly Reason"]].head(5).to_string(index=False))


# =============================================================================
# SECTION 10: MATPLOTLIB / SEABORN STATIC VISUALIZATIONS
# =============================================================================

# Dark theme to match Power BI dashboard aesthetic
plt.style.use("dark_background")
COLORS = {
    "blue":  "#4A9EFF",
    "gold":  "#F0B840",
    "green": "#7ADC9A",
    "red":   "#FF6B6B",
    "bg":    "#0D1117",
    "card":  "#131920",
    "text":  "#E8E4DC",
    "muted": "#8A8E9A",
}

fig, axes = plt.subplots(2, 3, figsize=(18, 11))
fig.patch.set_facecolor(COLORS["bg"])
fig.suptitle("Global Sales Intelligence Dashboard",
             color=COLORS["text"], fontsize=18, fontweight="bold", y=1.01)

# --- Plot 1: Revenue by Region (Horizontal Bar) ---
ax = axes[0, 0]
ax.set_facecolor(COLORS["card"])
bars = ax.barh(regional_summary["Region"], regional_summary["Revenue"],
               color=COLORS["blue"], alpha=0.85, height=0.55)
ax.bar_label(bars, fmt="$%.0f", label_type="edge",
             color=COLORS["text"], fontsize=9, padding=4)
ax.set_title("Revenue by Region", color=COLORS["text"], fontsize=12, pad=10)
ax.tick_params(colors=COLORS["muted"])
ax.set_xlabel("Revenue ($)", color=COLORS["muted"], fontsize=9)
for spine in ax.spines.values():
    spine.set_edgecolor(COLORS["card"])

# --- Plot 2: Revenue by Category (Donut Chart) ---
ax = axes[0, 1]
ax.set_facecolor(COLORS["card"])
wedge_colors = [COLORS["blue"], COLORS["gold"], COLORS["green"]]
wedges, texts, autotexts = ax.pie(
    category_summary["Revenue"],
    labels=category_summary["Category"],
    autopct="%1.1f%%",
    colors=wedge_colors,
    startangle=90,
    wedgeprops={"width": 0.55, "edgecolor": COLORS["bg"], "linewidth": 2},
    pctdistance=0.75
)
for t in texts:
    t.set_color(COLORS["muted"]); t.set_fontsize(9)
for at in autotexts:
    at.set_color(COLORS["text"]); at.set_fontsize(8)
ax.set_title("Revenue by Category", color=COLORS["text"], fontsize=12, pad=10)

# --- Plot 3: Revenue by Segment (Bar) ---
ax = axes[0, 2]
ax.set_facecolor(COLORS["card"])
bar_colors = [COLORS["blue"], COLORS["gold"], COLORS["green"]]
bars = ax.bar(segment_summary["Segment"], segment_summary["Revenue"],
              color=bar_colors, alpha=0.85, width=0.5)
ax.bar_label(bars, fmt="$%.0f", color=COLORS["text"], fontsize=9, padding=4)
ax.set_title("Revenue by Segment", color=COLORS["text"], fontsize=12, pad=10)
ax.tick_params(colors=COLORS["muted"])
ax.set_ylabel("Revenue ($)", color=COLORS["muted"], fontsize=9)
for spine in ax.spines.values():
    spine.set_edgecolor(COLORS["card"])

# --- Plot 4: Monthly Revenue Trend + 3M Moving Average ---
ax = axes[1, 0]
ax.set_facecolor(COLORS["card"])
x = range(len(monthly_trend))
ax.fill_between(x, monthly_trend["Revenue"], alpha=0.12, color=COLORS["blue"])
ax.plot(x, monthly_trend["Revenue"], color=COLORS["blue"],
        linewidth=1.5, label="Monthly Revenue", alpha=0.8)
ax.plot(x, monthly_trend["Moving_Avg_3M"], color=COLORS["gold"],
        linewidth=2, linestyle="--", label="3M Moving Avg")
ax.set_title("Revenue Trend + 3M Moving Average", color=COLORS["text"], fontsize=12, pad=10)
ax.tick_params(colors=COLORS["muted"], labelbottom=False)
ax.legend(facecolor=COLORS["card"], edgecolor=COLORS["muted"],
          labelcolor=COLORS["text"], fontsize=8)
for spine in ax.spines.values():
    spine.set_edgecolor(COLORS["card"])

# --- Plot 5: YoY Growth Bar ---
ax = axes[1, 1]
ax.set_facecolor(COLORS["card"])
growth = yoy["YoY Growth %"].fillna(0)
bar_cols = [COLORS["green"] if v >= 0 else COLORS["red"] for v in growth]
bars = ax.bar(yoy["Year"].astype(str), growth, color=bar_cols, alpha=0.85, width=0.5)
ax.bar_label(bars, fmt="%.1f%%", color=COLORS["text"], fontsize=9, padding=4)
ax.axhline(y=0, color=COLORS["muted"], linewidth=0.8, linestyle="--")
ax.set_title("Year-over-Year Revenue Growth %", color=COLORS["text"], fontsize=12, pad=10)
ax.tick_params(colors=COLORS["muted"])
for spine in ax.spines.values():
    spine.set_edgecolor(COLORS["card"])

# --- Plot 6: Anomaly Detection Scatter ---
ax = axes[1, 2]
ax.set_facecolor(COLORS["card"])
normal = df[~df.index.isin(anomalies.index)]
ax.scatter(normal["Sales"], normal["Profit"],
           alpha=0.25, s=12, color=COLORS["blue"], label="Normal")
ax.scatter(anomalies["Sales"], anomalies["Profit"],
           alpha=0.8, s=40, color=COLORS["red"],
           marker="X", zorder=5, label=f"Anomaly ({len(anomalies)})")
ax.axhline(y=0, color=COLORS["muted"], linewidth=0.8, linestyle="--")
ax.set_title("Anomaly Detection: Sales vs Profit", color=COLORS["text"], fontsize=12, pad=10)
ax.set_xlabel("Sales ($)", color=COLORS["muted"], fontsize=9)
ax.set_ylabel("Profit ($)", color=COLORS["muted"], fontsize=9)
ax.tick_params(colors=COLORS["muted"])
ax.legend(facecolor=COLORS["card"], edgecolor=COLORS["muted"],
          labelcolor=COLORS["text"], fontsize=8)
for spine in ax.spines.values():
    spine.set_edgecolor(COLORS["card"])

plt.tight_layout()
plt.savefig("global_sales_dashboard.png", dpi=150,
            bbox_inches="tight", facecolor=COLORS["bg"])
plt.show()
print("\n✅ Dashboard saved: global_sales_dashboard.png")


# =============================================================================
# SECTION 11: INTERACTIVE PLOTLY DASHBOARD
# =============================================================================

fig_plotly = make_subplots(
    rows=2, cols=3,
    subplot_titles=(
        "Revenue by Region", "Revenue by Category",
        "Revenue by Segment", "Monthly Revenue Trend",
        "YoY Growth %", "Anomaly Detection"
    ),
    specs=[
        [{"type": "bar"}, {"type": "pie"}, {"type": "bar"}],
        [{"type": "scatter"}, {"type": "bar"}, {"type": "scatter"}]
    ],
    vertical_spacing=0.14,
    horizontal_spacing=0.08
)

# Row 1 Col 1 — Region
fig_plotly.add_trace(go.Bar(
    x=regional_summary["Revenue"], y=regional_summary["Region"],
    orientation="h", marker_color="#4A9EFF",
    name="Region", text=regional_summary["Revenue"].apply(lambda x: f"${x:,.0f}"),
    textposition="outside"
), row=1, col=1)

# Row 1 Col 2 — Category Pie
fig_plotly.add_trace(go.Pie(
    labels=category_summary["Category"],
    values=category_summary["Revenue"],
    hole=0.5,
    marker_colors=["#4A9EFF", "#F0B840", "#7ADC9A"],
    name="Category"
), row=1, col=2)

# Row 1 Col 3 — Segment
fig_plotly.add_trace(go.Bar(
    x=segment_summary["Segment"], y=segment_summary["Revenue"],
    marker_color=["#4A9EFF", "#F0B840", "#7ADC9A"],
    name="Segment", text=segment_summary["Revenue"].apply(lambda x: f"${x:,.0f}"),
    textposition="outside"
), row=1, col=3)

# Row 2 Col 1 — Monthly Trend
fig_plotly.add_trace(go.Scatter(
    x=monthly_trend["Month"], y=monthly_trend["Revenue"],
    mode="lines", line=dict(color="#4A9EFF", width=2),
    fill="tozeroy", fillcolor="rgba(74,158,255,0.08)",
    name="Revenue"
), row=2, col=1)
fig_plotly.add_trace(go.Scatter(
    x=monthly_trend["Month"], y=monthly_trend["Moving_Avg_3M"],
    mode="lines", line=dict(color="#F0B840", width=2, dash="dash"),
    name="3M Moving Avg"
), row=2, col=1)

# Row 2 Col 2 — YoY
bar_colors_yoy = ["#7ADC9A" if v >= 0 else "#FF6B6B"
                   for v in yoy["YoY Growth %"].fillna(0)]
fig_plotly.add_trace(go.Bar(
    x=yoy["Year"].astype(str),
    y=yoy["YoY Growth %"].fillna(0),
    marker_color=bar_colors_yoy, name="YoY Growth",
    text=yoy["YoY Growth %"].fillna(0).apply(lambda x: f"{x:.1f}%"),
    textposition="outside"
), row=2, col=2)

# Row 2 Col 3 — Anomaly Scatter
fig_plotly.add_trace(go.Scatter(
    x=normal["Sales"], y=normal["Profit"],
    mode="markers",
    marker=dict(color="#4A9EFF", size=4, opacity=0.3),
    name="Normal"
), row=2, col=3)
fig_plotly.add_trace(go.Scatter(
    x=anomalies["Sales"], y=anomalies["Profit"],
    mode="markers",
    marker=dict(color="#FF6B6B", size=9, symbol="x", opacity=0.9),
    name=f"Anomaly ({len(anomalies)})"
), row=2, col=3)

fig_plotly.update_layout(
    title=dict(
        text="Global Sales Intelligence Dashboard — Interactive View",
        font=dict(size=18, color="#E8E4DC")
    ),
    plot_bgcolor="#131920",
    paper_bgcolor="#0D1117",
    font=dict(color="#8A8E9A", size=11),
    showlegend=True,
    legend=dict(bgcolor="#131920", bordercolor="#1E2530",
                borderwidth=1, font=dict(color="#E8E4DC")),
    height=750,
)
fig_plotly.update_xaxes(gridcolor="#1E2530", zerolinecolor="#1E2530")
fig_plotly.update_yaxes(gridcolor="#1E2530", zerolinecolor="#1E2530")

fig_plotly.write_html("global_sales_dashboard_interactive.html")
print("✅ Interactive dashboard saved: global_sales_dashboard_interactive.html")


# =============================================================================
# SECTION 12: SUMMARY EXPORT
# =============================================================================

with pd.ExcelWriter("global_sales_summary.xlsx", engine="openpyxl") as writer:
    df.to_excel(writer, sheet_name="Raw Data", index=False)
    regional_summary.to_excel(writer, sheet_name="Regional", index=False)
    category_summary.to_excel(writer, sheet_name="Category", index=False)
    segment_summary.to_excel(writer, sheet_name="Segment", index=False)
    top_products.to_excel(writer, sheet_name="Top Products", index=False)
    monthly_trend.to_excel(writer, sheet_name="Monthly Trend", index=False)
    anomalies.to_excel(writer, sheet_name="Anomalies", index=False)

print("✅ Excel summary saved: global_sales_summary.xlsx")
print("\n🏁 All outputs generated successfully.")
