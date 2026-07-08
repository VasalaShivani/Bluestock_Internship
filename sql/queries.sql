-- 1. Top 5 funds by 5-Year Return 
SELECT df.scheme_name, fp."5y_return"
FROM fact_performance fp
JOIN dim_fund df ON fp.amfi_code = df.amfi_code
ORDER BY fp."5y_return" DESC
LIMIT 5;

-- 2. Average NAV per month
SELECT strftime('%Y-%m', nav_date) AS month, AVG(nav) AS avg_nav
FROM fact_nav
GROUP BY strftime('%Y-%m', nav_date)
ORDER BY month DESC;

-- 3. SIP inflow YoY growth
SELECT 
    t1.month_year AS Current_Month,
    t1.sip_inflow_cr AS Current_Inflow,
    t2.sip_inflow_cr AS Last_Year_Inflow,
    ROUND(((t1.sip_inflow_cr - t2.sip_inflow_cr) / t2.sip_inflow_cr) * 100, 2) AS YoY_Growth_Pct
FROM fact_sip_inflows t1
LEFT JOIN fact_sip_inflows t2 
    ON substr(t1.month_year, 1, 4) - 1 || substr(t1.month_year, 5) = t2.month_year;

-- 4. Transactions by state
SELECT state, COUNT(*) as total_transactions, SUM(amount) as total_volume
FROM fact_transactions
GROUP BY state
ORDER BY total_volume DESC;

-- 5. Funds with expense_ratio < 1%
SELECT df.scheme_name, fp.expense_ratio
FROM fact_performance fp
JOIN dim_fund df ON fp.amfi_code = df.amfi_code
WHERE fp.expense_ratio < 1.0
ORDER BY fp.expense_ratio ASC;

-- 6. Total Lumpsum vs SIP volume
SELECT transaction_type, SUM(amount) as total_invested
FROM fact_transactions
GROUP BY transaction_type;

-- 7. Count of funds with negative Sharpe ratio
SELECT COUNT(*) as funds_with_negative_sharpe
FROM fact_performance
WHERE negative_sharpe_flag = 1;

-- 8. Top 5 funds by 3-year return
SELECT df.scheme_name, fp."3y_return"
FROM fact_performance fp
JOIN dim_fund df ON fp.amfi_code = df.amfi_code
ORDER BY fp."3y_return" DESC
LIMIT 5;

-- 9. Number of schemes per Fund House
SELECT fund_house, COUNT(amfi_code) as total_schemes
FROM dim_fund
GROUP BY fund_house
ORDER BY total_schemes DESC;

-- 10. Daily Return volatility (Max vs Min NAV)
SELECT amfi_code, MAX(nav) as highest_nav, MIN(nav) as lowest_nav, ROUND((MAX(nav) - MIN(nav)), 2) as absolute_variance
FROM fact_nav
GROUP BY amfi_code;