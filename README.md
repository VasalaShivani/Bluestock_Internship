```markdown
# Bluestock Mutual Fund Analytics Platform 
---

## Project Overview
The Indian mutual fund industry has scaled exponentially, managing over ₹81 lakh crore in AUM across 1,908 schemes and 26.12 crore investor folios as of December 2025[cite: 1]. However, retail investors and financial advisors often struggle with fragmented text/PDF formats and a lack of unified systems to track risk-adjusted performance across Asset Management Companies (AMCs)[cite: 1].

This individual capstone project builds a full-stack financial technology data platform that automates live and historical data extraction from AMFI India, mfapi.in, and market indices, routes it through a robust ETL pipeline into a normalized SQLite star schema, and delivers dynamic, stakeholder-ready visualizations[cite: 1].

---

## Technical Stack Details

| Category | Tool / Library | Version | Purpose |
| :--- | :--- | :--- | :--- |
| **Language** | Python | 3.10+ | Core pipeline, ETL, and analytical computations[cite: 1] |
| **Data Manipulation** | Pandas | 2.0+ | DataFrames processing, forward-fills, and parsing[cite: 1] |
| **Numerical & Risk** | NumPy | 1.24+ | Vector operations, risk metric formulations[cite: 1] |
| **Database Engine** | SQLite3 / SQLAlchemy | Built-in / 2.0 | Local relational database storage and Python mapping[cite: 1] |
| **Statistics** | SciPy | 1.10+ | OLS regression to compute Alpha and Beta metrics[cite: 1] |
| **HTTP Client / API** | Requests / JSON | 2.30+ | Live JSON NAV data fetching from mfapi.in API[cite: 1] |
| **Visualization** | Power BI Desktop | Latest | Production-grade 4-page interactive reporting dashboard[cite: 1] |

---

## Repository Folder Structure & Catalog

The repository maps exactly to the following project-compliant structural guidelines[cite: 1]:

```text
bluestock_mf_capstone/
├── data/
│   ├── raw/                 # Ingested primary CSV sets and API payloads[cite: 1]
│   └── processed/           # Sanitized, type-cast, forward-filled flat files[cite: 1]
├── db/
│   └── bluestock_mf.db      # Production-ready normalized SQLite Database file[cite: 1]
├── notebooks/
│   ├── EDA_analysis.ipynb          # Exploratory analysis with 15+ complex charts[cite: 1]
│   ├── performance_analytics.ipynb # Mathematical formulation of risk arrays[cite: 1]
│   └── advanced_analytics.ipynb    # VaR, CVaR, and investor cohort matrices[cite: 1]
├── scripts
│   ├── data_ingestion.py      # Environment validation & ingestion steps[cite: 1]
│   ├── data_cleaning.py  
│   ├── etl_pipeline.py      # Master operational script orchestrating the pipeline[cite: 1]
│   ├── compute_metrics.py   # Automated background performance evaluations[cite: 1]
│   ├── live_nav_fetch.py    # Public endpoint micro-fetcher for mfapi.in data[cite: 1]
│   └── recommender.py       # Algorithmic fund recommendations based on risk grade[cite: 1]
├── sql/
│   ├── schema.sql           # CREATE TABLE DDL schema for Star Schema modeling[cite: 1]
│   └── queries.sql          # 10 production-ready analytical SQL query checks[cite: 1]
├── dashboard/
│   └── bluestock_mf.pbix    # Interactive Power BI Workbook file[cite: 1]
├── reports/
│   ├── Final_Report.pdf     # 15-20 page publication-ready formal documentation[cite: 1]
│   └── Presentation.pptx    # 12-slide executive presentation deck[cite: 1]
└── README.md                # System deployment guide

```

---

##  Dataset Inventory Reference

The platform parses and cross-maps **10 structured datasets** (comprising over 87K rows of data spanning 4.5 years):

* **`01_fund_master.csv` (40 rows)**: Scheme tracking codes, AMC details, sub-categories, managers, expense ratios, and SEBI risk categories.


* **`02_nav_history.csv` (~46,000 rows)**: Historical daily NAV timelines from Jan 2022 to May 2026, anchored to real AMFI values via mfapi.in.


* **`03_aum_by_fund_house.csv` (~90 rows)**: Quarterly Assets Under Management (in ₹ Crore) tracking the top 10 large fund houses from 2022 to 2025.


* **`04_monthly_sip_inflows.csv` (48 rows)**: AMFI monthly logs showing active SIP accounts, monthly inflows, and total assets.


* **`05_category_inflows.csv` (~144 rows)**: Sector categories net capital movements for FY 2024-25.


* **`06_industry_folio_count.csv` (21 rows)**: Timeline of overall mutual fund folio milestones split by asset type.


* **`07_scheme_performance.csv` (40 rows)**: Formulated metrics (CAGR returns, Sharpe, Alpha, Beta, Drawdowns) computed across files.


* **`08_investor_transactions.csv` (~32,000 rows)**: Simulated transaction behavior log tracing 5,000 regional investors across state and city tiers.


* **`09_portfolio_holdings.csv` (~320 rows)**: Equity equity component logs breaking down stock weights and sector balances as of Dec 2025.


* **`10_benchmark_indices.csv` (~8,000 rows)**: Closing daily indices metrics (Nifty 50, Nifty 100, BSE SmallCap) used as performance baselines.



---

##  Relational Schema Engineering

Data transforms into a high-speed relational star schema optimized on `amfi_code` and temporal date keys:

* **Dimensions**: `dim_fund` (40 schemes), `dim_date` (1,500 trading entries).


* **Facts**: `fact_nav` (46K records), `fact_transactions` (32K+ orders), `fact_performance`, `fact_portfolio`, `fact_aum`, `fact_sip_industry`.



---

##  Financial Mathematics Implemented

All calculations handle localized business day logic and trading tracking parameters:

* **Compound Annual Growth Rate (CAGR)**:



$$\text{CAGR} = \left(\frac{\text{NAV}_{\text{End}}}{\text{NAV}_{\text{Start}}}\right)^{\frac{1}{n}} - 1$$


* **Sharpe Ratio**: Uses standard annualized trading variance benchmarks scaled against a risk-free proxy ($R_f = 6.5\%$):



$$\text{Sharpe} = \frac{R_p - R_f}{\sigma_p \cdot \sqrt{252}}$$


* **Alpha & Market Beta**: Derived via Ordinary Least Squares (OLS) tracking regressions comparing historical daily return movements against the Nifty 100 benchmark.


* **95% Historical Value at Risk (VaR)**: Isolates the 5th percentile line of historical returns to track downside safety margin levels.



---

##  Execution & Testing Protocol

### 1. Setup Environment

Clone the workspace and initialize python dependencies:

```bash
git clone [https://github.com/VasalaShivani/Bluestock_Internship.git](https://github.com/VasalaShivani/Bluestock_Internship.git)
cd Bluestock_Internship
pip install -r requirements.txt

```

### 2. Run End-to-End ETL Pipeline Orchestrator

Execute the script pipeline layer to extract data from APIs, clean files, apply holiday forward-fills, and automatically construct your `bluestock_mf.db` tables:

```bash
python scripts/etl_pipeline.py

```

### 3. Verify Database Queries

Verify relational state counts directly via the SQLite terminal interface script mapping:

```bash
sqlite3 db/bluestock_mf.db < sql/queries.sql

```

---

## Power BI Dashboard Structural Setup

The integrated business analytics workspace `bluestock_mf.pbix` is split into **4 analytical visual layouts**:

1. **Page 1 - Industry Overview**: Global KPI cards showing ₹81L Crore industry footprint metrics, ₹31,002 Crore record SIP inflows, and folio timeline expansions.


2. **Page 2 - Fund Performance**: Risk vs reward scatter metrics, rolling alpha distributions, and tabular comparative scorecards with multi-AMC slicer filtering.


3. **Page 3 - Investor Analytics**: Demographic trends profiling transaction behavior distributions across Top-30 and Beyond-30 geographic tiers.


4. **Page 4 - SIP & Market Trends**: Trend alignment timelines comparing monthly retail inflows directly alongside index benchmarks.



---

## ⚖️ Disclaimer

All raw attributes are compiled from publicly documented AMFI India, NSE, and BSE sheets for study, assessment, and training evaluations at Bluestock Fintech Pvt. Ltd. It does not signify regulated financial advice.

```

```
