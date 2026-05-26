# Portfolio VaR Analysis Engine

A quantitative risk-modeling tool built from first principles in native Python. This engine connects directly to live market data streams via the Yahoo Finance API to calculate empirical risk boundaries for custom asset portfolios without relying on third-party analytical frameworks like Pandas or NumPy.

## Core Engineering Features
* **Automated Data Cleaning:** Handles mismatched historical trading day lengths across multiple concurrent asset feeds, ensuring perfect chronological alignment of returns.
* **Matrix Ingestion Pipeline:** Features a nested loop architecture to map user-defined allocation weights against raw asset price deltas, transforming independent time-series data streams into a single, unified portfolio return distribution.
* **Empirical Statistical Mapping:** Implements non-parametric sorting to extract precise distribution thresholds at variable confidence parameters (90%, 95%, 99%), translating abstract probability into maximum expected capital-at-risk dollar figures.

##  How to Run the Tool
Ensure you have the native Python `requests` module installed:
```bash
pip install requests
