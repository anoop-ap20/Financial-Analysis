**Dow Jones Index Analysis**

**Objective**

To analyze Dow Jones stock data, predict future price trends, and identify hidden patterns using Supervised and Unsupervised Machine Learning techniques.

📌 *Key Questions*:
1. Can we predict whether a stock's price will increase or decrease next week?
2. Can we cluster stocks into different categories based on price behavior?
3. What insights can we extract from historical stock trends?

**Methodology**

*Step 1*: Build your own SQL Database Management System [(DBMS)](Dow-Jones-Index/DowJones_DB.sql) with historical data. Run [SQL queries](Dow-Jones-Index/DowJones_Queries.sql) to filter relevant columns and export the results as a [CSV](Dow-Jones-Index/dow_jones_index_ml.csv) for further analysis.

*Step 2*: Perform data cleaning & feature engineering (i.e. convert string to float, handle missing values, and standardize numerical data)

*Step 3*: [Supervised Learning](https://github.com/anoop-ap20/Financial-Analysis/blob/e9d7eaba057e113381879d43d49d96d3735eda40/Dow-Jones-Index/Supervised%3A%20Predict%20Stock%20Price%20Movement.py) - Stock Price prediction. Predict if the next week's stock price will increase or decrease. 1-Increases, 0-Decreases. 
    
    Models Used:
      - Logistic Regression → Baseline model
      - Random Forest Classifier → Non-linear relationships
      - Neural Network (ANN) → Deep learning approach
    Evaluation:
      - Use Accuracy, Precision, Recall, F1-score to measure performance
      - Compare models using a classification report

![Supervised Learning](https://github.com/anoop-ap20/Financial-Analysis/blob/7eeb71f3b65fd78cc5ca0f83bed38ccf7cf32565/Dow-Jones-Index/PNGs/Supervised%20Learning.png)

*Step 4*: [Unsupervised Learning 1](https://github.com/anoop-ap20/Financial-Analysis/blob/e9d7eaba057e113381879d43d49d96d3735eda40/Dow-Jones-Index/Unsupervised%3A%20Stock%20Grouping%20e%20Segmentation.py) & [Unsupervised Learning 2](https://github.com/anoop-ap20/Financial-Analysis/blob/e9d7eaba057e113381879d43d49d96d3735eda40/Dow-Jones-Index/Unsupervised%3A%20Stock%20Market%20Pattern%20Identification.py)- Stock Clustering. Group similar stocks based on financial indicators

    Models Used:
      - DBSCAN (Density-Based Clustering)
      - Agglomerative Clustering (Hierarchical)
    Evaluation
      - Silhouette Score
      - Davies-Bouldin Index
      - Calinski-Harabasz Score
    Visualize Clusters

![Unsupervised Learning 1](https://github.com/anoop-ap20/Financial-Analysis/blob/7eeb71f3b65fd78cc5ca0f83bed38ccf7cf32565/Dow-Jones-Index/PNGs/Unsupervised%20Learning%201.png)
![Unsupervised Learning 2](https://github.com/anoop-ap20/Financial-Analysis/blob/7eeb71f3b65fd78cc5ca0f83bed38ccf7cf32565/Dow-Jones-Index/PNGs/Unsupervised%20Learning%202.png)
![Visualize Clusters](https://github.com/anoop-ap20/Financial-Analysis/blob/f173df64f0696038353235bd5d2621d5acc9c700/Dow-Jones-Index/PNGs/Visualize%20Clusters.png)

**Conclusion**

1. Random Forest model performed better than Logistic Regression but still has low accuracy (~60%). Neural Network needs further training.
2. Agglomerative Clustering grouped stocks into 3 distinct behavior categories, helping investors understand stock trends.
3. DBSCAN clustering returned only one label: -1, meaning all data points were classified as noise and no clusters were formed.
