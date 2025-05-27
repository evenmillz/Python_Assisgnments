# Console Output for Assignment

## Terminal Command
`python statistics_probability.py`

## Output
Number of rows: 30
Number of columns: 7
Descriptive Statistics:
        column_1   column_2  feature_1  feature_2     target
count  30.000000  30.000000  30.000000  30.000000  30.000000
mean    2.556667   1.620000   1.310000   0.626667   0.733333
std     0.473201   0.539732   0.282049   0.219613   0.449776
min     1.600000   0.800000   0.800000   0.100000   0.000000
25%     2.225000   1.225000   1.100000   0.500000   0.250000
50%     2.600000   1.600000   1.300000   0.700000   1.000000
75%     2.900000   1.900000   1.500000   0.800000   1.000000
max     3.300000   2.900000   1.900000   0.900000   1.000000
Probability: 0.45233992408227036
T-statistic: 2.9209979971514985
P-value: 0.00912185731115502
Correlation Matrix:
           column_1  column_2  feature_1  feature_2    target
column_1   1.000000  0.875699  -0.314428   0.588864 -0.137174
column_2   0.875699  1.000000  -0.359255   0.495719 -0.176136
feature_1 -0.314428 -0.359255   1.000000  -0.344039  0.483839
feature_2  0.588864  0.495719  -0.344039   1.000000 -0.169894
target    -0.137174 -0.176136   0.483839  -0.169894  1.000000
Regression Analysis Results:
                            OLS Regression Results
==============================================================================
Dep. Variable:                 target   R-squared:                       0.236
Model:                            OLS   Adj. R-squared:                  0.113
Method:                 Least Squares   F-statistic:                     1.927
Date:                Mon, 26 May 2025   Prob (F-statistic):              0.137
Time:                        22:26:06   Log-Likelihood:                -14.059
No. Observations:                  30   AIC:                             38.12
Df Residuals:                      25   BIC:                             45.12
Df Model:                           4
Covariance Type:            nonrobust
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const         -0.3566      0.709     -0.503      0.619      -1.816       1.103
column_1       0.0832      0.372      0.224      0.825      -0.682       0.849
column_2      -0.0582      0.308     -0.189      0.852      -0.693       0.577
feature_1      0.7633      0.306      2.492      0.020       0.132       1.394
feature_2     -0.0453      0.455     -0.100      0.921      -0.982       0.891
==============================================================================
Omnibus:                        2.710   Durbin-Watson:                   1.458
Prob(Omnibus):                  0.258   Jarque-Bera (JB):                2.218
Skew:                          -0.542   Prob(JB):                        0.330
Kurtosis:                       2.227   Cond. No.                         35.6
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.