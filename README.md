# HW4_ETF_ranking

## Description 

|  ETF  | Sharpe-Omega  | ASKSR-Value | Riskiness    |
| ------------- | ------------- |------------- |------------- | 
| ETF1  | 1  | 3  | 3  | 
| ETF2  | 2  | 2  | 1  | 

When finish all the ETF ranking by weekly and monthly, 
we could utilize the spearman's rank correlation to test the rank between week and month. 
Moreover, if the correlation is above 0.7, we then use data by weekly. 

## The Indicators Rank of ETFs in weekly frequency

| ETF  | Sharpe-Omega | S_Rank | ASKSR-Value | A_Rank | Riskiness   | R_Rank |
|------|-------------|--------|-------------|--------|-------------|--------|
| FPA  | 0.908515    | 29     | 28.1090246  | 25     | -           | -      |
| FPXI | 1.227656    | 3      | 24.74757981 | 27     | 1.48E-06    | 1      |
| IQDE | 1.032982    | 23     | 39.85869959 | 9      | 0.00796245  | 24     |
| IQDY | 1.107187    | 16     | 32.4097691  | 20     | 0.000341761 | 13     |
| CHIQ | 1.157367    | 11     | 33.90015122 | 17     | 0.00156666  | 19     |
| GEM  | 1.195171    | 5      | 32.18097678 | 21     | 0.000190356 | 8      |
| ADRA | 1.037718    | 22     | 36.83762474 | 13     | 0.00367994  | 22     |
| PAF  | 1.028545    | 24     | 28.69464283 | 24     | 0.00217739  | 21     |
| IEMG | 1.202105    | 4      | 39.06803153 | 10     | 0.000228369 | 10     |
| HEEM | 1.057868    | 21     | 33.12356553 | 19     | 0.0140492   | 25     |
| AXJV | 0.949393    | 28     | 17.10552934 | 29     | 0.546783    | 27     |
| EMGF | 1.171963    | 7      | 27.34601678 | 26     | 0.000516204 | 16     |
| ACWX | 1.144497    | 13     | 37.63009317 | 12     | 4.50E-05    | 6      |
| AAXJ | 1.167515    | 8      | 34.56840976 | 16     | 0.000389331 | 14     |
| EEMA | 1.162804    | 10     | 35.80030982 | 15     | 0.000572542 | 17     |
| AIA  | 1.192318    | 6      | 33.41809882 | 18     | 0.000244934 | 12     |
| IPOS | 1.091952    | 19     | 40.20279081 | 7      | 0.000616928 | 18     |
| CWI  | 1.142671    | 14     | 40.08630201 | 8      | 4.21E-05    | 5      |
| QEMM | 1.167366    | 9      | 58.75049091 | 2      | 0.000193937 | 9      |
| MOTI | 1.265989    | 2      | 68.51424483 | 1      | 1.60E-06    | 2      |
| REMX | 1.01355     | 26     | 21.82142093 | 28     | -           | -      |
| VEU  | 1.145684    | 12     | 36.55234455 | 14     | 4.12E-05    | 4      |
| VXUS | 1.140072    | 15     | 38.4912342  | 11     | 5.50E-05    | 7      |
| AXJL | 1.016862    | 25     | 47.56574373 | 4      | 0.0267384   | 26     |
| EMCG | 1.103721    | 17     | 31.54705211 | 22     | 0.0060045   | 23     |
| XSOE | 1.327659    | 1      | 29.66511586 | 23     | 2.23E-06    | 3      |
| DNL  | 1.097952    | 18     | 57.13268259 | 3      | 0.00164884  | 20     |
| IHDG | 1.08365     | 20     | 43.39231286 | 6      | 0.00042334  | 15     |
| DBAP | 1.012345    | 27     | 45.07861144 | 5      | 0.000240228 | 11     |


## The Indicators Rank of ETFs in monthly frequency


| ETF  | Sharpe-Omega | S_Rank | ASKSR-Value | A_Rank | Riskiness   | R_Rank |
|------|-------------|--------|-------------|--------|-------------|--------|
| FPA  | 1.191266    | 29     | 18.74949311 | 12     | 0.0119976   | 28     |
| FPXI | 1.680224    | 6      | 18.52673767 | 14     | 2.20E-05    | 17     |
| IQDE | 1.367341    | 25     | 21.48498913 | 4      | 2.26E-05    | 18     |
| IQDY | 1.68861     | 4      | 25.94961609 | 2      | 1.65E-06    | 5      |
| CHIQ | 1.502871    | 18     | 15.51259132 | 26     | 0.000754618 | 26     |
| GEM  | 1.535936    | 16     | 16.9972229  | 21     | 1.56E-05    | 15     |
| ADRA | 1.60525     | 7      | 21.90055194 | 3      | 8.39E-07    | 1      |
| PAF  | 1.411269    | 22     | 20.2090751  | 8      | 2.29E-05    | 19     |
| IEMG | 1.593653    | 9      | 17.30911687 | 20     | 9.75E-06    | 13     |
| HEEM | 1.538975    | 15     | 31.38060001 | 1      | 2.57E-06    | 6      |
| AXJV | 1.291698    | 28     | 16.07720021 | 24     | 0.008491085 | 27     |
| EMGF | 1.56381     | 13     | 17.41024929 | 18     | 3.78E-05    | 21     |
| ACWX | 1.467374    | 19     | 19.43672474 | 11     | 4.70E-06    | 10     |
| AAXJ | 1.570686    | 12     | 17.31454667 | 19     | 3.82E-05    | 22     |
| EEMA | 1.60337     | 8      | 16.72941199 | 23     | 3.33E-05    | 20     |
| AIA  | 1.775134    | 1      | 20.81698656 | 6      | 1.95E-05    | 16     |
| IPOS | 1.304544    | 27     | 15.9186108  | 25     | 0.000416967 | 24     |
| CWI  | 1.584798    | 10     | 18.10928411 | 16     | 1.16E-06    | 4      |
| QEMM | 1.697129    | 3      | 17.94880184 | 17     | 9.34E-07    | 2      |
| MOTI | 1.437105    | 21     | 16.92724422 | 22     | 6.68E-05    | 23     |
| REMX | 1.309678    | 26     | 14.40261809 | 29     | 0.09512381  | 29     |
| VEU  | 1.505482    | 17     | 18.30193331 | 15     | 3.54E-06    | 7      |
| VXUS | 1.456981    | 20     | 19.47215987 | 10     | 8.30E-06    | 12     |
| AXJL | 1.68656     | 5      | 21.15206023 | 5      | 1.14E-06    | 3      |
| EMCG | 1.3771      | 24     | 14.63884998 | 28     | 0.00050845  | 25     |
| XSOE | 1.739528    | 2      | 14.81034794 | 27     | 1.26E-05    | 14     |
| DNL  | 1.58229     | 11     | 20.17408637 | 9      | 4.43E-06    | 9      |
| IHDG | 1.400029    | 23     | 20.67383106 | 7      | 5.08E-06    | 11     |
| DBAP | 1.551789    | 14     | 18.62501285 | 13     | 3.61E-06    | 8      |

## Rank Correlation 

### Correlation between monthly and weekly rankings.
We have the Spearman rank correlation and Kendall rank correlation
We test the weekly rank and monthly rank of ETFs, in order to validate the stability of indicators

footnote: Some ETFs Riskiness are not able to caculated by solver(expected excess return is negative), therefore we choose to ignore the nan value of these.  


| Indicators | Riskness      | Sharpe-Omega    | ASKSR |  
| ------------- | ------------- |------------- |------------- | 
|Spearman | 0.1575 | 0.5227  | 0.2448  | 
|Kandall  | 0.1168  | 0.3940  | 0.1626  | 

We strongly believe that the indicators performance rankings are quite different in weekly frequency and monthly frequency.  
Following the statemtent of Prof. Shih, we suggest to use monthly frequency because all the correlation are not above 0.7.  

Both spearman and kandall indicate that the Sharpe-omega has highest validity than others. 


### Correlation among different risk indicators
Here we compare the rankings of different risk indicators. Again, we apply both Spearman and Kendall rank correlation on the monthly and weekly data.

* Among all of the combinations, we can see that Sharpe-Omega and Riskiness pair shows higher correlation than other combinations in three tables. Although it is not the highest in the monthly Spearman correlation matrix, the correlation is still not low.
* The Sharpe-Omega and Riskiness pair shows higher correlation in weekly data than in monthly data.
* The ASKSR and Riskiness pair shows significantly higher correlation in monthly data than in weekly data.
* The Sharpe-Omega and ASKSR pair shows negative correlation in weekly data, while positive in monthly data.


| Spearman_weekly | Sharpe-Omega | ASKSR | Riskiness |
|-----------------|-------------|-------|-----------|
| Sharp-Omega     | 1           | 　    | 　        |
| ASKSR           | -0.152      | 1     | 　        |
| Riskiness       | 0.724       | 0.101 | 1         |


| Kendall_weekly | Sharpe-Omega | ASKSR | Riskiness |
|-------------------|-------------|-------|-----------|
| Sharp-Omega       | 1           | 　    | 　        |
| ASKSR             | -0.145      | 1     | 　        |
| Riskiness         | 0.556       | 0.060 | 1         |


| Spearman_monthly | Sharpe-Omega | ASKSR | Riskiness |
|------------------|-------------|-------|-----------|
| Sharp-Omega      | 1           | 　    | 　        |
| ASKSR            | 0.243       | 1     | 　        |
| Riskiness        | 0.618       | 0.630 | 1         |


| Kendall_monthly | Sharpe-Omega | ASKSR | Riskiness |
|--------------------|-------------|-------|-----------|
| Sharp-Omega        | 1           | 　    | 　        |
| ASKSR              | 0.138       | 1     | 　        |
| Riskiness          | 0.453       | 0.448 | 1         |
