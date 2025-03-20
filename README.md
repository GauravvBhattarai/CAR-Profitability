# Capital Adequacy and Bank Profitability Analysis

This project analyzes the relationship between capital adequacy indicators and profitability metrics in the banking sector. Using data from 15 Nepalese commercial banks over a 15-year period (2008-2022), the analysis examines how capital adequacy ratios and other financial indicators impact bank profitability.

# A. Problem Statement

- What is the existing capital adequacy position of selected banks?
- How do capital adequacy indicators influence bank profitability?
- What is the relationship between capital adequacy ratio and bank's exposure to credit risk?

# B. Dataset 

The dataset includes 15 commercial banks in Nepal with financial indicators from 2008-2022:

- Government-owned banks: Rastriya Banijya Bank, Nepal Bank Limited, Agricultural Development Bank
- Joint venture banks: Standard Chartered Bank, Himalayan Bank, Everest Bank, Nepal SBI Bank
- Private banks: Nabil Bank, Sanima Bank, Citizens Bank International, NMB Bank, Siddhartha Bank, Machhapuchhre Bank, Prime Commercial Bank, NIC Asia Bank

# C. Methodology

- Research Design: Descriptive and analytical approach using panel data regression

- Models: Fixed Effects and Random Effects models with Hausman test for model selection
  
- Variables:
        - Dependent: Return on Equity (ROE)
        - Independent: Capital Adequacy Ratio (CAR), Advances to Assets Ratio (AAR), Government Securities to Total Investment (GSIT), Non-Performing Loans Ratio (NPL)
  
- Rationale of the study: Looking a few years back, from 2010 to the present, the Nepalese banking industry has experienced various reforms dedicated to enhancing operational efficiency to compete in the fast-paced international finance sector. This study aims to show the relationship between capital adequacy and profitability of the commercial bank. This research will help to understand the capital adequacy and profitability position along with understanding the existing risk-taking position of the selected commercial bank. Throughout the research, various quantitative and statistical approaches for determining the relationship between the variables will be deeply studied and interpreted. Similarly, this research will also facilitate financial institutions, potential investors and financial analysts in investment decision-making.  Since the banks generally operate in an environment with a high degree of uncertainty which results in exposure to many types of risks, this research will be helpful to minimize those risks while preventing the bank from going through financial crises that affect the national economy.

# D. Findings

## 1. Descriptive Statistics

![image](https://github.com/user-attachments/assets/f1c53e27-83bc-499f-8132-06dc24377a52)

## 2. Regression Results

Based on the Hausman test (p-value = 0.88), the Random Effects model is more appropriate for this analysis:
- Capital Adequacy Ratio (CAR): Negative relationship with ROE, suggesting that higher capital requirements might reduce profitability
- Government Securities to Total Investment (GSIT): Positive and statistically significant relationship with ROE (coefficient = 13.54, p-value = 0.0003)
- Advances to Assets Ratio (AAR): Negative relationship with ROE, indicating that aggressive lending might lead to lower profitability
- Non-Performing Loans (NPL): Negative relationship with ROE, as expected

Model Fit
- R-squared: 74.87% (Random Effects Model)
- F-statistic: 164.62 (p-value < 0.001)

# E. Conclusion 

Study of analyzing the determinants of commercial bank profitability in Nepal shows that inclusion of external factors such as the shape the size of bank, industry specific factors like concentration and banking sector development, macroeconomic variables like GDP growth, inflation rate and exchange rate and other profitability indicators like ROA would have made differences in the results. Further studies can address other Capital adequacy indicators, absolute number of branches and annual inflation rate, net interest margin etc., while conducting their studies. Simultaneous negative relationship between capital and profitability provides recommendations for banks to improve market performance by managing and make use of capital in an efficient way. Large amount of capital or quality loans might generate high CAR for banks, but reduces the amount of profit in long run. To maintain an adequate level of capital as directed by the NRB, besides raising equity’s capital, banks also can reduce risk-weighted assets, this in turn can help them with the BASEL regulatory framework as well.

Some researches around the world have shown positive relationship of CAR when ROA is taken as their profitability indicator. But as the finance basics suggest, for developing economies like Nepal, ROE would be a better measure. This paper does not study the in-depth implications of BASEL III accord which could have major impact upon the results and the outcome. The outcomes of this paper furnish proof regarding the endogeneity of the capital ratio. With the absence of any systematic correlation between the capital held and the profitability observed within the realm of banking, it can be inferred that the diverse capital ratios emerged as consequences of competitive markets functioning perfectly. In such a scenario, these markets would erase any structured connection between the capital amount and the overall performance of the banks. Another significant discovery from this study indicates a significant and negative reduction in profitability for all banks associated with the Common Equity Tier 1 capital ratio (CAR). This suggests that as a bank's financial stability increases, its profit generation tends to decrease which in line opposes and contradicts the theoretical understanding of capital sufficiency as praised a lot by the recent Basel III regulations. These regulations aim to enhance the soundness and stability of the global banking system by urging banks to enhance their capital resilience to achieve greater profitability. The primary deduction is that credit risk exerts a favorable influence on profitability when gauged using NPL in proportion to total assets, ROA. Inversely, the CAR exhibits an unfavorable impact on profitability when measured through ROE, which in the case of Nepal is one of the best predictors of profitability position of banks. On a policy level, considering the differential effect of credit risk on profitability, this paper supports the fact that there isn't a universal solution to an adequate capital level that maximizes profitability. Hence, distinct policy directives are necessary for all class of banks in Nepal. Given the association between NPLs and ROE, the paper advises commercial banks to take measures aimed at enhancing their strategies for managing credit risk. This will consequently bolster their operational efficiency. On the other hand, with regards to the connection between CAR and profitability, this paper advises policymakers not to enforce a blanket application of CAR policies, because elevating the capital requisites of banks with the intention of augmenting their financial robustness does not guarantee increased profitability over time.

# F. Implications and Recommendation

Based on the detailed analysis certain implication and recommendation can be made on the capital adequacy and relationship between capital adequacy position and financial performance of the commercial banks.

- An optimal capital level helps to create balance between capital adequacy and profitability. If a bank holds a higher degree of CAR, it might affect the profitability of the bank due to the higher amount of unused capital fund. So, it is recommended for banks to hold an optimal capital level.
- The advances to asset ratios show negative relationship between advances to asset ratio. It means that if a bank gives away loan without proper analysis it may be riskier towards higher default. Thus, it is recommended for banks to make a proper analysis before lending.
- Government securities are one of the safest forms of debt instrument as an increase in government security leads to an increase in profitability. It is less risky in nature so bank is recommended to invest more on government securities.
- An increase in nonperforming loan decreases the profitability of bank as NPL and ROE have negative relationship with each other. As presented in the data the NPL of banks is increasing which has caused a decreased in its net profit. So, it is important for banks to make effective policies and analysis to reduce the level of non-performing loan.
- This project recommends that NRB to ensure that the gains of the banking reform processes are sustained, more decisive measures aimed at tightening the risk management framework in the commercial banking sector will create a positive effect on the profitability positions of banks.

# G. Appendices

- Overall Statistics of the Data

![image](https://github.com/user-attachments/assets/0023ab0c-e2e5-437c-9ae8-e47fd85a4ef8)

- Correlation between the selected variables

![image](https://github.com/user-attachments/assets/1be1852f-cb92-479a-8bef-c709deb626bd)

- Fixed Effect Model

![image](https://github.com/user-attachments/assets/1e04c2ba-6d2a-44fd-8d20-0d7a55bc85d5)

- Random Effect Model

![image](https://github.com/user-attachments/assets/3b7398a7-826f-4ab5-abc9-85afd56834aa)

- Results after using the robust 

![image](https://github.com/user-attachments/assets/e6005cc7-9430-47f5-8ec9-a6849c9a4159)

















