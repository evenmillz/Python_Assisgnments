import pandas as pd
import numpy as np
from scipy.stats import norm
from scipy.stats import ttest_ind
import statsmodels.api as sm
import warnings

# Load the dataset
dataset = pd.read_csv('dataset_1.csv')

# Data analysis
num_rows, num_cols = dataset.shape
print(f"Number of rows: {num_rows}")
print(f"Number of columns: {num_cols}")

# Descriptive Statistics: Summary statistics that provide information 
# about the distribution (how the data is spread out), 
# central tendency (the typical or average value), 
# and variability (how the data points differ from each other) of the data.
summary_stats = dataset.describe()
print("Descriptive Statistics:")
print(summary_stats)

# Probability calculation: The likelihood of an event occurring, 
# represented as a decimal or percentage.
if len(dataset) >= 8:
    prob = norm.cdf(2.5, loc=dataset['column_1'].mean(), scale=dataset['column_1'].std())
    print(f"Probability: {prob}")
else:
    print("Insuffient data points for probability calculation.")
    # mean = dataset['value'].mean()
    # std_dev = dataset['value'].std()
    # print(f"Mean: {mean}, Standard Deviation: {std_dev}")

    # # Calculate the probability of a value being less than a certain threshold
    # threshold = 50
    # probability = norm.cdf(threshold, loc=mean, scale=std_dev)
    # print(f"Probability of value being less than {threshold}: {probability:.4f}")

# Hypothesis Testing: A statistical method to test assumptions about a population based on sample data.
# T-statistic: A measure of how statistically significant the difference between two groups is in a t-test (a statistical test to compare means of two groups).
# P-value: The probability of obtaining the observed results (or more extreme) if the null hypothesis (assumption of no significant difference or relationship) is true (a measure of the evidence against the null hypothesis).
warnings.filterwarnings("ignore")
group_a_data = dataset[dataset['group'] == 'A']['column_2']
group_b_data = dataset[dataset['group'] == 'B']['column_2']

if len(group_a_data) >= 8 and len(group_b_data) >= 8:
    t_statistic, p_value = ttest_ind(group_a_data, group_b_data)
    print(f"T-statistic: {t_statistic}")
    print(f"P-value: {p_value}")
else:
    print("Insuffient data points for hypothesis testing.")

    # Interpret the p-value
    # alpha = 0.05  # Significance level
    # if p_value < alpha:
    #     print("Reject the null hypothesis: There is a significant difference between the groups.")
    # else:
    #     print("Fail to reject the null hypothesis: No significant difference between the groups.")

# Correlation Analysis: A statistical method to measure the strength and direction of the relationship between two variables.
# Correlation Matrix: A table that shows the correlation coefficients between variables in a dataset, indicating the strength and direction of the relationships (how variables are related to each other).
numeric_columns = dataset.select_dtypes(include=[np.number]).columns
corr_matrix = dataset[numeric_columns].corr()
print("Correlation Matrix:")
print(corr_matrix)

# Regression Analysis: A statistical method to model the relationship between a dependent variable (the outcome we want to predict) and one or more independent variables (the predictors or features).
# Coefficient: In the context of regression analysis (analyzing the relationship between variables to predict outcomes), it represents the estimated effect or impact of an independent variable on the dependent variable.
if len(dataset) >= 8:
    X = dataset[['column_1', 'column_2', 'feature_1', 'feature_2']]  # Independent variables
    y = dataset['target']  # Dependent variable
    X = sm.add_constant(X)  # Add a constant term for the intercept
    model = sm.OLS(y, X).fit()  # Fit the Ordinary Least Squares regression model
    print("Regression Analysis Results:")
    print(model.summary())
else:
    print("Insuffient data points for regression analysis.")
# Standard Error: An estimate of the standard deviation (measure of the variability of a set of values) of the sampling distribution (variability from different data collection instances) of a statistic, typically used to measure the precision or accuracy of an estimated parameter.

# R-squared: A statistical measure that represents the proportion of the variance in the dependent variable that can be explained by the independent variables in a regression model (a statistical model that estimates the relationship between dependent and independent variables).

# Adj. R-squared: The adjusted R-squared is a modified version of R-squared that accounts for the number of predictors (variables used to predict or explain an outcome) in the model, providing a more reliable measure of model fit (degree of agreement between the model's predictions and the actual data).

# F-statistic: A statistical test that determines the overall significance of a regression model (a statistical model that estimates the relationship between dependent and independent variables) by comparing the explained variance to the unexplained variance.

# Dependent Variable: The variable being predicted or explained by the independent variables in a regression model (a statistical model that estimates the relationship between dependent and independent variables).

# OLS Regression: Ordinary Least Squares regression, a common method used to estimate the parameters of a linear regression model (a statistical model that estimates the relationship between dependent and independent variables) by minimizing the sum of squared residuals (the measure of the difference between observed and predicted values, magnified for analysis).

# AIC: Akaike Information Criterion, a measure of the relative quality of a statistical model that balances model fit with model complexity. Named after the Japanese statistician (Hirotugu Akaike) who developed it as a measure for model selection and evaluation.

# BIC: Bayesian Information Criterion, a measure of the relative quality of a statistical model that penalizes model complexity more than AIC. Named after Thomas Bayes, an English mathematician and theologian who introduced Bayes' theorem (a mathematical formula that calculates the probability of an event based on prior knowledge or beliefs and new evidence or observations).

# Covariance: A statistical measure that quantifies the relationship and variability between two variables.

# Covariance Matrix: A square matrix that summarizes the covariance (statistical measure that quantifies relationship and variability) between multiple variables, indicating the strength and direction of their linear relationships.

# Covariance Type: Specifies the method used to estimate the covariance matrix (a square matrix that provides information about the relationships and variability between multiple variables) of the regression model (a statistical model that estimates the relationship between dependent and independent variables), affecting the standard errors and hypothesis tests (tests that evaluate statistical significance of observed data against a hypothesis).

# Durbin-Watson: A statistic used to test for the presence of autocorrelation (correlation between residuals) in a regression model (a statistical model that estimates the relationship between dependent and independent variables). Named after statisticians James Durbin and Geoffrey Watson, who developed the test.

# Omnibus: A statistical test that assesses the normality assumption of the residuals (difference between observed and predicted values) in a regression model (a statistical model that estimates the relationship between dependent and independent variables).

# Symmetry: Balance or equality in a statistical distribution or data set. Asymmetry is the opposite (a lack of symmetry in a statistical distribution or data set).

# Peakedness: Peaked refers to the characteristic of a distribution that indicates the degree of concentration of data around its central point. A distribution with higher peakedness is more concentrated around its mean, while a distribution with lower peakedness is flatter and more spread out.

# Jarque-Bera (JB): A statistical test that assesses the normality assumption of the residuals based on skewness (measure of asymmetry [a lack of symmetry in a statistical distribution or data set] in a probability distribution) and kurtosis (measure of the shape and peakedness [defined above] of a statistical distribution.

# Skew: A measure of the asymmetry (a lack of symmetry in a statistical distribution or data set) of a probability distribution.

# Kurtosis: A measure of the peakedness (defined above) or flatness of a probability distribution. The term kurtosis originates from the Greek word kurtos, meaning “curved” or “arched.” It was introduced by the statistician Karl Pearson.

# Cond. No.: Condition Number, a measure of the sensitivity of a regression model (a statistical model that estimates the relationship between dependent and independent variables) to changes in the data, indicating multicollinearity (high correlation between predictors).