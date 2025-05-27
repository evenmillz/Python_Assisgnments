# Console Output for Challenge

## Terminal Command
`python statistics_probability.py`

## Output 1
000  30.000000  30.000000  30.000000  30.000000
mean    5.233333   3.020000   1.310000   0.626667   0.733333
std     8.336390   5.008159   0.282049   0.219613   0.449776
min     1.600000   0.800000   0.800000   0.100000   0.000000
25%     2.300000   1.225000   1.100000   0.500000   0.250000
50%     2.650000   1.600000   1.300000   0.700000   1.000000
75%     2.975000   2.075000   1.500000   0.800000   1.000000
max    33.300000  25.900000   1.900000   0.900000   1.000000
Probability: 0.3715013024268728
T-statistic: 1.195346583557072
P-value: 0.24746322423975084
Correlation Matrix:
           column_1  column_2  feature_1  feature_2    target
column_1   1.000000 -0.043865  -0.289498   0.176924 -0.025137
column_2  -0.043865  1.000000  -0.202764   0.124907 -0.199620
feature_1 -0.289498 -0.202764   1.000000  -0.344039  0.483839
feature_2  0.176924  0.124907  -0.344039   1.000000 -0.169894
target    -0.025137 -0.199620   0.483839  -0.169894  1.000000
Regression Analysis Results:
                            OLS Regression Results
==============================================================================
Dep. Variable:                 target   R-squared:                       0.257
Model:                            OLS   Adj. R-squared:                  0.138
Method:                 Least Squares   F-statistic:                     2.160
Date:                Mon, 26 May 2025   Prob (F-statistic):              0.103
Time:                        22:29:30   Log-Likelihood:                -13.636
No. Observations:                  30   AIC:                             37.27
Df Residuals:                      25   BIC:                             44.28
Df Model:                           4
Covariance Type:            nonrobust
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const         -0.2990      0.548     -0.545      0.590      -1.428       0.830
column_1       0.0062      0.010      0.636      0.531      -0.014       0.026
column_2      -0.0084      0.016     -0.524      0.605      -0.041       0.024
feature_1      0.7904      0.308      2.565      0.017       0.156       1.425
feature_2     -0.0169      0.378     -0.045      0.965      -0.796       0.762
==============================================================================
Omnibus:                        2.002   Durbin-Watson:                   1.510
Prob(Omnibus):                  0.367   Jarque-Bera (JB):                1.722
Skew:                          -0.464   Prob(JB):                        0.423
Kurtosis:                       2.282   Cond. No.                         86.5
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.

## Output 2
Number of rows: 30
Number of columns: 7
Descriptive Statistics:
         column_1    column_2  feature_1  feature_2     target
count   30.000000   30.000000  30.000000  30.000000  30.000000
mean    25.133333   14.320000   1.310000   0.626667   0.733333
std     70.890753   44.228134   0.282049   0.219613   0.449776
min      1.600000    0.800000   0.800000   0.100000   0.000000
25%      2.300000    1.325000   1.100000   0.500000   0.250000
50%      2.700000    1.600000   1.300000   0.700000   1.000000
75%      3.200000    2.350000   1.500000   0.800000   1.000000
max    333.100000  222.300000   1.900000   0.900000   1.000000
Probability: 0.3747606617868996
T-statistic: 1.183665392248761
P-value: 0.251942412289254
Correlation Matrix:
           column_1  column_2  feature_1  feature_2    target
column_1   1.000000 -0.023409  -0.158680   0.213679 -0.216871
column_2  -0.023409  1.000000  -0.303504   0.167723 -0.056579
feature_1 -0.158680 -0.303504   1.000000  -0.344039  0.483839
feature_2  0.213679  0.167723  -0.344039   1.000000 -0.169894
target    -0.216871 -0.056579   0.483839  -0.169894  1.000000
Regression Analysis Results:
                            OLS Regression Results
==============================================================================
Dep. Variable:                 target   R-squared:                       0.262
Model:                            OLS   Adj. R-squared:                  0.143
Method:                 Least Squares   F-statistic:                     2.213
Date:                Mon, 26 May 2025   Prob (F-statistic):             0.0965
Time:                        22:31:05   Log-Likelihood:                -13.542
No. Observations:                  30   AIC:                             37.08
Df Residuals:                      25   BIC:                             44.09
Df Model:                           4
Covariance Type:            nonrobust
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const         -0.3070      0.532     -0.577      0.569      -1.403       0.789
column_1      -0.0009      0.001     -0.788      0.438      -0.003       0.001
column_2       0.0009      0.002      0.481      0.635      -0.003       0.005
feature_1      0.7867      0.305      2.582      0.016       0.159       1.414
feature_2      0.0308      0.382      0.081      0.936      -0.756       0.817
==============================================================================
Omnibus:                        1.883   Durbin-Watson:                   1.537
Prob(Omnibus):                  0.390   Jarque-Bera (JB):                1.578
Skew:                          -0.417   Prob(JB):                        0.454
Kurtosis:                       2.248   Cond. No.                         637.
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.