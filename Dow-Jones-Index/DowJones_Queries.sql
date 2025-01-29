USE DowJones_DB;
/* Verify the Tables */
SELECT * FROM Stock;
SELECT * FROM Market;
SELECT * FROM Factors;

/* Stock Price Trends */
CREATE INDEX idx_record ON Market(record);
SELECT 
    M.ticker,
    S.stock_ID,
    M.record,
    M.m_quarter,
    M.m_open AS Open_Price,
    M.m_close AS Close_Price,
    M.high AS High_Price,
    M.low AS Low_Price
FROM 
    Market M
JOIN 
    Stock S ON M.ticker = S.ticker
WHERE 
    M.m_quarter BETWEEN 1 AND 2
ORDER BY 
    M.record DESC;

/* Dividend Analysis */
SELECT 
    F.ticker,
    F.record,
    F.days_to_next_dividend,
    F.percent_return_next_dividend,
    M.m_open AS Open_Price_Before_Dividend,
    M.m_close AS Close_Price_Before_Dividend,
    N.m_open AS Open_Price_After_Dividend,
    N.m_close AS Close_Price_After_Dividend
FROM 
    Factors F
JOIN 
    Market M ON F.ticker = M.ticker AND F.record = M.record
LEFT JOIN 
    Market N ON F.ticker = N.ticker 
    AND N.record = F.record + INTERVAL F.days_to_next_dividend DAY
WHERE 
    F.ticker IN ('AA' , 'BAC')
ORDER BY 
    F.record DESC;

/* Volume vs. Price Analysis */
SELECT 
    M.ticker,
    M.record,
    M.volume AS Trading_Volume,
    (M.m_close - M.m_open) AS Price_Change,
    ((M.m_close - M.m_open) / M.m_open) * 100 AS Price_Percent_Change
FROM 
    Market M
WHERE 
    M.ticker IN ('HPQ', 'JNJ') 
    AND M.record BETWEEN '2011-01-14' AND '2011-05-31' 
ORDER BY 
    M.record DESC;

/* Price Trends (Gain, Loss, No Change) */
CREATE VIEW Price_Trend_View AS
SELECT 
    m.ticker, 
    m.record, 
    m.m_open, 
    m.m_close,
    CASE
        WHEN m.m_close > m.m_open THEN 'Gain'
        WHEN m.m_close < m.m_open THEN 'Loss'
        ELSE 'No Change'
    END AS Price_Trend
FROM Market m;
-- Once the view is created, it can be queried independently using the statement below
SELECT * FROM Price_Trend_View WHERE record = '2011-03-18';

/* Price Volatility - Ranked Top 10 Changes */
CREATE INDEX idx_high_low ON Market(high, low);
SELECT m.ticker, m.record, (m.high - m.low) AS Price_Change
FROM Market m
WHERE m.m_quarter = 2
ORDER BY Price_Change DESC
LIMIT 10;

/* Verify dependencies */
SELECT
    S.ticker, 
    S.stock_ID, 
    M.record, 
    M.m_quarter, 
    M.m_open, 
    M.m_close,
    M.next_weeks_open,
    M.next_weeks_close,
    M.high, 
    M.low, 
    M.volume, 
    M.previous_weeks_volume,
    F.percent_change_volume_over_last_wk,
    F.percent_change_next_weeks_price,
    F.days_to_next_dividend, 
    F.percent_return_next_dividend
FROM Stock S
LEFT JOIN 
    Market M ON S.ticker = M.ticker
LEFT JOIN 
    Factors F ON S.ticker = F.ticker AND M.record = F.record
ORDER BY 
    M.record DESC; 
-- The query results can also be exported as a CSV file for use in ML analysis

-- Thank You for sticking around till the end! 
-- If any of these queries runs forever, blame the joins... not me. HeHe.
