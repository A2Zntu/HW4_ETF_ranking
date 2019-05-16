# HW4_ETF_ranking

## Description 

|  ETF  | Sharp-Omega  | ASKSR-Value | Riskiness    |
| ------------- | ------------- |------------- |------------- | 
| ETF1  | 1  | 3  | 3  | 
| ETF2  | 2  | 2  | 1  | 

When finish all the ETF ranking by weekly and monthly, 
we could utilize the spearman's rank correlation to test the rank between week and month. 
Moreover, if the correlation is above 0.7, we then use data by weekly. 

## The Indicators Rank of ETFs in weekly frequency

| ETF  | Sharp-Omega | S_Rank | ASKSR-Value | A_Rank | Riskiness   | R_Rank |
|------|-------------|--------|-------------|--------|-------------|--------|
| FPA  | 0.908515    | 29     | 28.1090246  | 25     | -           | -      |
| FPXI | 1.227656    | 3      | 24.74757981 | 27     | -           | -      |
| IQDE | 1.032982    | 23     | 39.85869959 | 9      | -           | -      |
| IQDY | 1.107187    | 16     | 32.4097691  | 20     | 0.000341737 | 12     |
| CHIQ | 1.157367    | 11     | 33.90015122 | 17     | 0.00156632  | 18     |
| GEM  | 1.195171    | 5      | 32.18097678 | 21     | 0.000190311 | 7      |
| ADRA | 1.037718    | 22     | 36.83762474 | 13     | -           | -      |
| PAF  | 1.028545    | 24     | 28.69464283 | 24     | 0.00217737  | 19     |
| IEMG | 1.202105    | 4      | 39.06803153 | 10     | 0.000228382 | 9      |
| HEEM | 1.057868    | 21     | 33.12356553 | 19     | -           | -      |
| AXJV | 0.949393    | 28     | 17.10552934 | 29     | 0.546407    | 20     |
| EMGF | 1.171963    | 7      | 27.34601678 | 26     | 0.000516201 | 15     |
| ACWX | 1.144497    | 13     | 37.63009317 | 12     | 4.50014E-05 | 5      |
| AAXJ | 1.167515    | 8      | 34.56840976 | 16     | 0.00038934  | 13     |
| EEMA | 1.162804    | 10     | 35.80030982 | 15     | 0.000572441 | 16     |
| AIA  | 1.192318    | 6      | 33.41809882 | 18     | 0.000244913 | 11     |
| IPOS | 1.091952    | 19     | 40.20279081 | 7      | 0.000622055 | 17     |
| CWI  | 1.142671    | 14     | 40.08630201 | 8      | 4.21344E-05 | 4      |
| QEMM | 1.167366    | 9      | 58.75049091 | 2      | 0.000193951 | 8      |
| MOTI | 1.265989    | 2      | 68.51424483 | 1      | 1.60369E-06 | 1      |
| REMX | 1.01355     | 26     | 21.82142093 | 28     | -           | -      |
| VEU  | 1.145684    | 12     | 36.55234455 | 14     | 4.11961E-05 | 3      |
| VXUS | 1.140072    | 15     | 38.4912342  | 11     | 5.49754E-05 | 6      |
| AXJL | 1.016862    | 25     | 47.56574373 | 4      | -           | -      |
| EMCG | 1.103721    | 17     | 31.54705211 | 22     | -           | -      |
| XSOE | 1.327659    | 1      | 29.66511586 | 23     | 2.23833E-06 | 2      |
| DNL  | 1.097952    | 18     | 57.13268259 | 3      | -           | -      |
| IHDG | 1.08365     | 20     | 43.39231286 | 6      | 0.000429094 | 14     |
| DBAP | 1.012345    | 27     | 45.07861144 | 5      | 0.000243047 | 10     |


## The Indicators Rank of ETFs in monthly frequency


| ETF  | Sharp-Omega | S_Rank | ASKSR-Value | A_Rank | Riskiness   | R_Rank |
|------|-------------|--------|-------------|--------|-------------|--------|
| FPA  | 1.191266    | 29     | 18.74949311 | 12     | 0.012032    | 24     |
| FPXI | 1.680224    | 6      | 18.52673767 | 14     | 2.19751E-05 | 13     |
| IQDE | 1.367341    | 25     | 21.48498913 | 4      | 2.25454E-05 | 14     |
| IQDY | 1.68861     | 4      | 25.94961609 | 2      | 1.64775E-06 | 1      |
| CHIQ | 1.502871    | 18     | 15.51259132 | 26     | 0.000755157 | 22     |
| GEM  | 1.535936    | 16     | 16.9972229  | 21     | 1.55924E-05 | 11     |
| ADRA | 1.60525     | 7      | 21.90055194 | 3      | -           | -      |
| PAF  | 1.411269    | 22     | 20.2090751  | 8      | 2.28907E-05 | 15     |
| IEMG | 1.593653    | 9      | 17.30911687 | 20     | 9.75195E-06 | 9      |
| HEEM | 1.538975    | 15     | 31.38060001 | 1      | 2.57344E-06 | 2      |
| AXJV | 1.291698    | 28     | 16.07720021 | 24     | 0.00850906  | 23     |
| EMGF | 1.56381     | 13     | 17.41024929 | 18     | 3.78258E-05 | 17     |
| ACWX | 1.467374    | 19     | 19.43672474 | 11     | 4.69466E-06 | 6      |
| AAXJ | 1.570686    | 12     | 17.31454667 | 19     | 3.81884E-05 | 18     |
| EEMA | 1.60337     | 8      | 16.72941199 | 23     | 3.33309E-05 | 16     |
| AIA  | 1.775134    | 1      | 20.81698656 | 6      | 0.000019462 | 12     |
| IPOS | 1.304544    | 27     | 15.9186108  | 25     | 0.000416891 | 20     |
| CWI  | 1.584798    | 10     | 18.10928411 | 16     | 0.999971    | 26     |
| QEMM | 1.697129    | 3      | 17.94880184 | 17     | -           | -      |
| MOTI | 1.437105    | 21     | 16.92724422 | 22     | 0.000066922 | 19     |
| REMX | 1.309678    | 26     | 14.40261809 | 29     | -           | -      |
| VEU  | 1.505482    | 17     | 18.30193331 | 15     | 3.54309E-06 | 3      |
| VXUS | 1.456981    | 20     | 19.47215987 | 10     | 8.29868E-06 | 8      |
| AXJL | 1.68656     | 5      | 21.15206023 | 5      | 0.999837    | 25     |
| EMCG | 1.3771      | 24     | 14.63884998 | 28     | 0.000508297 | 21     |
| XSOE | 1.739528    | 2      | 14.81034794 | 27     | 1.25577E-05 | 10     |
| DNL  | 1.58229     | 11     | 20.17408637 | 9      | 4.43489E-06 | 5      |
| IHDG | 1.400029    | 23     | 20.67383106 | 7      | 0.000005086 | 7      |
| DBAP | 1.551789    | 14     | 18.62501285 | 13     | 3.61174E-06 | 4      |



## Rank Correlation 

We have the Spearman rank correlation and Kendall rank correlation
We test the weekly rank and monthly rank of ETFs, in order to validate the stability of indicators

footnote: Some ETFs Riskiness are not able to caculated by solver, therefore we choose to ignore the nan value of these.  


| Indicators | Riskness      | Sharp-Omega    | ASKSR |  
| ------------- | ------------- |------------- |------------- | 
|Spearman | 0.3614  | 0.5227  | 0.2448  | 
|Kandall  | 0.2865  | 0.3940  | 0.1626  | 

We strongly believe that the indicators performance rankings are quite different in weekly frequency and monthly frequency.  
Following the statemtent of Prof. Shih, we suggest to use monthly frequency because all the correlation are not above 0.7.  

Both spearman and kandall indicate that the Sharp-omage has highest validity than others. 
