**Portfolio Optimization and Analysis**

**Objective**

Analyzed and compared the performance of an optimal portfolio, S&P 500, and a risk-free investment to study the risk-return trade-off. Applied Markowitz Portfolio Theory to optimize asset allocation and evaluated performance using Sharpe ratio and historical trends.

**Methodology**

1. *Stock Selection*: Collected historical data of 10 random stocks from [Yahoo Finance](https://finance.yahoo.com/). Used financial ratios (debt, current, quick, inventory turnover, total asset turnover, and profit margin) to filter stocks. [Sheet: Summary](https://github.com/anoop-ap20/Financial-Analysis/blob/15e18ebfff0e76b77769280459cf6410d985f991/Portfolio%20Optimization%20and%20Analysis/Portfolio%20Optimization%20and%20Analysis.xlsx)
2. *Portfolio Optimization*: Applied Markowitz Theory to determine optimal stock weightage based on two different expected daily returns, comparing them to a minimum variance portfolio. [Sheet: Markowitz](https://github.com/anoop-ap20/Financial-Analysis/blob/15e18ebfff0e76b77769280459cf6410d985f991/Portfolio%20Optimization%20and%20Analysis/Portfolio%20Optimization%20and%20Analysis.xlsx)
3. *Performance Evaluation*: Calculated key metrics—Daily & Annual Return, Variance, Standard Deviation, Portfolio Beta, Jensen’s Alpha, and Sharpe Ratio—for optimized portfolios.

  ![Portfolio Selection](https://github.com/anoop-ap20/Financial-Analysis/blob/a8404e454c3fbf6a8441de812525c999a4e5efd8/Portfolio%20Optimization%20and%20Analysis/PNGs/Stock%20Weightage.png)
   
5. *Short Selling Constraint*: Ensured no short selling by adjusting weight allocations. [Sheet: My Portfolio](https://github.com/anoop-ap20/Financial-Analysis/blob/15e18ebfff0e76b77769280459cf6410d985f991/Portfolio%20Optimization%20and%20Analysis/Portfolio%20Optimization%20and%20Analysis.xlsx)
6. *Backtesting*: Used historical data for optimization and tested performance on recent 3-week data. [Sheet: Value at Risk](https://github.com/anoop-ap20/Financial-Analysis/blob/15e18ebfff0e76b77769280459cf6410d985f991/Portfolio%20Optimization%20and%20Analysis/Portfolio%20Optimization%20and%20Analysis.xlsx)
7. *Comparison*: Compared a $1,000,000 investment in the Optimal Portfolio vs. S&P 500 vs. Risk-Free Portfolio.

![Portfolio Comparison Chart](https://github.com/anoop-ap20/Financial-Analysis/blob/a8404e454c3fbf6a8441de812525c999a4e5efd8/Portfolio%20Optimization%20and%20Analysis/PNGs/Portfolio%20Comparison%20Chart.png)


**Tools & Techniques**

- Excel Functions: PIVOT TABLES, MMULT, nested IF-AND/OR, INDEX-MATCH for scenario analysis.
- Risk & Return Metrics: Sharpe Ratio, Portfolio Beta, Jensen’s Alpha.

**Conclusion**
1. *Diversification*: Ensure portfolios include assets with low or negative correlations to minimize volatility while maintaining returns. Using correlation matrix and Markowitz optimization during portfolio selection.

2. *Risk vs. Return Balance*: Use risk-adjusted return metrics, such as Sharpe ratios, to evaluate potential assets. Adjust portfolio allocations to maintain a balanced risk-return profile.

3. *Liquidity*: Prioritize liquid assets and monitor bid-ask spreads when choosing stocks. Ensure the portfolio has sufficient liquidity for rebalancing or unexpected withdrawals.

4. *Asset Weighting*: Rebalance periodically to maintain intended allocations. Utilize benchmarks like the S&P 500 as indicator of stable returns.

5. *Historical Data*: Perform historical analysis to identify trends (i.e. patterns) and outliers, but complement this with forward-looking estimates and scenario testing.
