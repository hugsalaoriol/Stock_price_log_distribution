# Price Difference Logarithm Analysis

This repository contains a data analysis and modeling project exploring the **fat-tailed, non-Gaussian behavior of logarithmic price differences** in financial markets. The study focuses on several key assets: the **S&P 500 (SP500)** index, **Gold**, **Crude Oil Brent**, and **JPMorgan Chase** stock.

---

## About the Project

This project investigates the statistical properties of price changes through logarithmic differences, demonstrating how financial returns deviate from the classic Gaussian (normal) distribution and exhibit fat tails. The analysis includes:

- Data collection and preprocessing for SP500, Gold, Crude Oil Brent, and JPMorgan Chase.
- Exploratory data analysis with graphical visualization.
- Statistical methods such as histogram comparisons, quantile-quantile plots, kurtosis analysis, and distribution fitting (Normal and Cauchy distributions).
- A detailed LaTeX report compiling the methodology, results, and conclusions.

---

## Contents

```
Stock_price_log_distribution/
├── main_analysis.py              # Python script with the full analysis
├── requirements.txt              # Required Python libraries
├── data/                         # (Optional) Folder for raw or processed datasets
├── results/
    └── report.pdf                # Final compiled PDF report
```

---

1. Clone this repository:

   ```bash
   git clone https://github.com/hugsalaoriol/price-difference-logarithm.git
   cd price-difference-logarithm
   ```

2. (Optional) Create and activate a Python virtual environment:

   ```bash
   python3 -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Open and run the Python file:

   ```bash
   python Price_differences.py
   ```

---

## Contact

**Hug Sala Oriol**  
Physics Student at University of Barcelona  
Email: hsalaoriol@gmail.com  
LinkedIn: [linkedin.com/in/hug-sala-oriol-b31280268](https://www.linkedin.com/in/hug-sala-oriol-b31280268)

---

## Future Work

- Extend analysis to additional financial instruments.
- Consider asymmetrical nature of log returns applying using the class of skewed generalized t type distributions.
- Include interactive visualizations for better insights.
- Implement interactive selection of stocks for analyisis.

---

Thank you for visiting! Feel free to explore the notebook and report, and contact me for any questions or collaborations.
