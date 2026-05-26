# Multi-Asset Portfolio Value at Risk (VaR) Engine

A quantitative risk-modeling tool built from first principles in native Python. This engine connects directly to live market data streams via the Yahoo Finance API to calculate empirical risk boundaries for custom asset portfolios without relying on third-party analytical frameworks like Pandas or NumPy.

## Core Engineering Features
* **Asymmetric Data Harmonization:** Automatically calculates the minimum common trading timeline across multiple concurrent tickers, dynamically slicing data streams to eliminate date-alignment errors caused by market halts or regional holidays.
* **Matrix Transformation Ingestion:** Features a nested-loop architecture that applies user-defined decimal weights to asset price deltas, synthesizing distinct data paths into a singular portfolio return distribution.
* **Empirical Risk Mapping:** Implements non-parametric sorting to extract precise 1-Day Value at Risk (VaR) thresholds at variable confidence parameters (e.g., 90%, 95%, 99%).

## 📊 How to Run the Tool
Ensure you have the native Python `requests` module installed:
```bash
pip install requests