<div align="center">

#  Numerical Integration Analysis
### Implementation of Newton-Cotes Formulas using Python

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![NumPy](https://img.shields.io/badge/NumPy-Analysis-013243?style=for-the-badge&logo=numpy)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-orange?style=for-the-badge&logo=plotly)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)

<p align="center">
  <b>A comprehensive study comparing Trapezoidal, Simpson's 1/3, and Simpson's 3/8 rules for numerical integration approximation and error analysis.</b>
</p>

</div>

---

## 👥 Team BD71 - Contributors
**Department of Computer Science and Engineering**

| SL | Student Name | ID | Role |
|:--:|:---|:---|:---|
| 1 | **MD NAHID MAHMUD** | 2024100000194 |  Project Manager & Report Lead |
| 2 | **ASHRAFUL KHAN** | 2024100000236 |  Lead Developer |
| 3 | **SHANTA CHANDRA RAKSHIT** | 2024100000235 |  Algorithm Specialist |
| 4 | **MOHAMMAD YEASIN** | 2023200000075 |  Data Analyst |
| 5 | **ANISUL HAQUE SHIHAB** | 2024100000168 |  Quality Assurance (QA) |
| 6 | **FATEMA AL ISLAM** | 2024100000161 |  Research Associate |
| 7 | **SHAJEDUL ISLAM FAHIM** | 2024100000434 |  Visual Designer |
| 8 | **MUHAMMAD SYDUL ISLAM** | 2024100000409 |  Documentation Specialist |
| 9 | **AINUN NAHAR KONA** | 2024100000433 |  Debugger |
| 10 | **FATEMA TABASSUM RIM** | 2024100000171 |  Presenter |

---

##  Key Features
* **Modular Architecture:** Separate modules for each integration algorithm (`trapezoidal.py`, `simpson13.py`, `simpson38.py`).
* **Dynamic Visualization:** Automatic generation of **Log-Log Convergence Plots** to visualize error reduction.
* **Robust Testing:** Validated against Trigonometric ($sin x$) and Polynomial ($x^3$) functions.
* **Exactness Verification:** Experimentally proves that Simpson's rules are exact for cubic polynomials.

---

##  Mathematical Background
This project implements the **Newton-Cotes** closed integration formulas:

### 1. Trapezoidal Rule
Approximates the area using linear segments:
$$I \approx \frac{h}{2} [f(x_0) + 2 \sum_{i=1}^{n-1} f(x_i) + f(x_n)]$$

### 2. Simpson's 1/3 Rule
Uses quadratic interpolation (Requires even $n$):
$$I \approx \frac{h}{3} [f(x_0) + 4 \sum_{odd} f(x_i) + 2 \sum_{even} f(x_i) + f(x_n)]$$

### 3. Simpson's 3/8 Rule
Uses cubic interpolation (Requires $n$ multiple of 3):
$$I \approx \frac{3h}{8} [f(x_0) + 3\sum f(x_{rest}) + 2\sum f(x_{multiples\_of\_3}) + f(x_n)]$$

---

## 📂 Repository Structure
```bash
Assignment_BD71/
├── src/                  # Core Logic
│   ├── main.py           # Entry point for the application
│   ├── trapezoidal.py    # Algorithm 1
│   ├── simpson13.py      # Algorithm 2
│   └── simpson38.py      # Algorithm 3
│
├── results/              # Output Graphs
│   ├── sinx_convergence.png
│   └── poly_convergence.png
│
├── requirements.txt      # Project Dependencies
└── README.md             # Documentation
