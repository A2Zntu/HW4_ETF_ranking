# HW4_ETF_ranking

## Description 

| ETF           | Riskness      | Omega    | ASKSR |  
| ------------- | ------------- |------------- |------------- | 
| ETF1  | 1  | 3  | 3  | 
| ETF2  | 2  | 2  | 1  | 

When finish all the ETF ranking by weekly and monthly, 
we could utilize the spearman's rank correlation to test the rank between week and month. 
Moreover, if the correlation is above 0.7, we then use data by weekly. 


## Rank Correlation 

We have the Spearman rank correlation and Kendall rank correlation
We test the weekly rank and monthly rank of ETFs, in order to validate the stability of indicators

| Indicators | Riskness      | Sharp-Omega    | ASKSR |  
| ------------- | ------------- |------------- |------------- | 
|Spearman | 0.3614  | 0.5227  | 0.2448  | 
|Kandall  | 0.2865  | 0.3940  | 0.1626  | 

We strongly believe that the indicators performance rankings are quite different in weekly frequency and monthly frequency.  
Following the statemtent of Prof. Shih, we suggest to use monthly frequency because all the correlation are not above 0.7.  
