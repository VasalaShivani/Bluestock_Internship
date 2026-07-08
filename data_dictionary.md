# Bluestock MF Analytics - Data Dictionary

### 1. dim_fund (Fund Master)
| Column Name  | Data Type | Description | Source |
| ------------- |:-------------:| :-----| :-----|
| amfi_code     | TEXT (PK) | Unique 6-digit identifier provided by AMFI | `01_fund_master.csv` |
| fund_house    | TEXT      | Name of the Asset Management Company | `01_fund_master.csv` |
| scheme_name   | TEXT      | Full operating name of the mutual fund | `01_fund_master.csv` |
| category      | TEXT      | Primary asset class (Equity, Debt, Hybrid) | `01_fund_master.csv` |
| sub_category  | TEXT      | Secondary asset class specialization | `01_fund_master.csv` |
| risk_grade    | TEXT      | Riskometer rating (Low to Very High) | `01_fund_master.csv` |

### 2. fact_nav (NAV History)
| Column Name  | Data Type | Description | Source |
| ------------- |:-------------:| :-----| :-----|
| nav_id        | INT (PK)  | Auto-incremented surrogate key | Generated |
| amfi_code     | TEXT (FK) | Maps to `dim_fund` | `02_nav_history.csv` |
| nav_date      | DATE      | Date of the specific NAV valuation | `02_nav_history.csv` |
| nav           | REAL      | Net Asset Value in INR | `02_nav_history.csv` |

### 3. fact_transactions (Investor Transactions)
| Column Name  | Data Type | Description | Source |
| ------------- |:-------------:| :-----| :-----|
| transaction_id| INT (PK)  | Auto-incremented surrogate key | Generated |
| amfi_code     | TEXT (FK) | Maps to `dim_fund` | `08_investor_transactions.csv` |
| investor_id   | TEXT      | Unique identifier for the investor | `08_investor_transactions.csv` |
| transaction_date| DATE    | Date transaction occurred | `08_investor_transactions.csv` |
| transaction_type| TEXT    | SIP, LUMPSUM, or REDEMPTION | `08_investor_transactions.csv` |
| amount        | REAL      | Transaction amount in INR (>0) | `08_investor_transactions.csv` |
| kyc_status    | TEXT      | KYC compliance status | `08_investor_transactions.csv` |
| state         | TEXT      | Geographical location of investor | `08_investor_transactions.csv` |

### 4. fact_performance (Scheme Performance)
| Column Name  | Data Type | Description | Source |
| ------------- |:-------------:| :-----| :-----|
| amfi_code     | TEXT (PK) | Maps to `dim_fund` | `07_scheme_performance.csv` |
| 1y_return     | REAL      | Trailing 1-year percentage return | `07_scheme_performance.csv` |
| 3y_return     | REAL      | Trailing 3-year percentage return | `07_scheme_performance.csv` |
| 5y_return     | REAL      | Trailing 5-year percentage return | `07_scheme_performance.csv` |
| expense_ratio | REAL      | Annual maintenance charge (0.1 - 2.5%) | `07_scheme_performance.csv` |
| sharpe_ratio  | REAL      | Risk-adjusted return metric | `07_scheme_performance.csv` |
| negative_sharpe_flag| INT | Boolean flag (1=True, 0=False) | Generated |

### 5. fact_sip_inflows (Monthly SIP Data)
| Column Name  | Data Type | Description | Source |
| ------------- |:-------------:| :-----| :-----|
| month_year    | TEXT (PK) | Month and year formatted as YYYYMM | `04_monthly_sip_inflows.csv` |
| sip_inflow_cr | REAL      | Total SIP inflows for the month in Crores | `04_monthly_sip_inflows.csv` |