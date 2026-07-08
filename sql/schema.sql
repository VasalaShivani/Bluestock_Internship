-- 1. Dimension Table: Fund Master
CREATE TABLE IF NOT EXISTS dim_fund (
    amfi_code TEXT PRIMARY KEY,
    fund_house TEXT,
    scheme_name TEXT,
    category TEXT,
    sub_category TEXT,
    risk_grade TEXT
);

-- 2. Fact Table: NAV History
CREATE TABLE IF NOT EXISTS fact_nav (
    nav_id INTEGER PRIMARY KEY AUTOINCREMENT,
    amfi_code TEXT,
    nav_date DATE,
    nav REAL,
    FOREIGN KEY (amfi_code) REFERENCES dim_fund(amfi_code)
);

-- 3. Fact Table: Investor Transactions
CREATE TABLE IF NOT EXISTS fact_transactions (
    transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
    amfi_code TEXT,
    investor_id TEXT,
    transaction_date DATE,
    transaction_type TEXT,
    amount REAL,
    kyc_status TEXT,
    state TEXT,
    FOREIGN KEY (amfi_code) REFERENCES dim_fund(amfi_code)
);

-- 4. Fact Table: Scheme Performance
CREATE TABLE IF NOT EXISTS fact_performance (
    amfi_code TEXT PRIMARY KEY,
    "1y_return" REAL,
    "3y_return" REAL,
    "5y_return" REAL,
    expense_ratio REAL,
    sharpe_ratio REAL,
    negative_sharpe_flag INTEGER,
    FOREIGN KEY (amfi_code) REFERENCES dim_fund(amfi_code)
);

-- 5. Fact Table: Monthly SIP Inflows
CREATE TABLE IF NOT EXISTS fact_sip_inflows (
    month_year TEXT PRIMARY KEY,
    sip_inflow_cr REAL
);