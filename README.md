<div align="center">

# Numerical Integration Analysis
### Precision Analysis of Newton-Cotes Formulas

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat&logo=python)
![NumPy](https://img.shields.io/badge/NumPy-Core-013243?style=flat&logo=numpy)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Plotting-orange?style=flat&logo=matplotlib)

<p align="center">
  <b>A comprehensive computational study comparing Trapezoidal, Simpson's 1/3, and Simpson's 3/8 rules for numerical integration and error convergence.</b>
</p>

</div>

---

## 📖 Project Overview
This project implements the **Newton-Cotes** closed integration formulas to solve definite integrals numerically. It is designed to demonstrate the accuracy, stability, and convergence rates of different numerical methods. The project includes automated graph generation for visual analysis of truncation errors.

---

## 👥 Team BD71 - Contributors
**Department of Computer Science and Engineering**

| Photo | Student Name | ID | Role |
|:---:|:---|:---|:---|
| <img src="https://github.com/nahidmahmud71.png" width="35" style="border-radius: 50%;" /> | **MD NAHID MAHMUD** | 2024100000194 | Project Manager & Report Lead |
| <img src="https://github.com/CodeByAshraful.png" width="35" style="border-radius: 50%;" /> | **ASHRAFUL KHAN** | 2024100000236 | Lead Developer |
| <img src="https://github.com/Shanto-SR.png" width="35" style="border-radius: 50%;" /> | **SHANTA CHANDRA RAKSHIT** | 2024100000235 | Algorithm Specialist |
| <img src="https://github.com/Yeasin145.png" width="35" style="border-radius: 50%;" /> | **MOHAMMAD YEASIN** | 2023200000075 | Data Analyst |
| <img src="https://github.com/shihab0p.png" width="35" style="border-radius: 50%;" /> | **ANISUL HAQUE SHIHAB** | 2024100000168 | Quality Assurance (QA) |
| <img src="https://github.com/itsfatema161.png" width="35" style="border-radius: 50%;" /> | **FATEMA AL ISLAM** | 2024100000161 | Research Associate |
| <img src="https://github.com/sif-fahim-434.png" width="35" style="border-radius: 50%;" /> | **SHAJEDUL ISLAM FAHIM** | 2024100000434 | Visual Designer |
| <img src="https://github.com/arponofcl-ctrl.png" width="35" style="border-radius: 50%;" /> | **MUHAMMAD SYDUL ISLAM** | 2024100000409 | Documentation Specialist |
| <img src="https://github.com/ainurkona78-stack.png" width="35" style="border-radius: 50%;" /> | **AINUN NAHAR KONA** | 2024100000433 | Debugger |
| <img src="https://github.com/fatemarim.png" width="35" style="border-radius: 50%;" /> | **FATAMA TABASSUM RIM** | 2024100000171 | Presenter |

---

## 🚀 Key Features
* **Consolidated Architecture:** All algorithms optimized within a single `main.py` file for portability.
* **Dynamic Visualization:** Automatically generates Area Plots and Convergence Plots.
* **Robust Testing:** Validated against Trigonometric ($sin x$) and Polynomial ($x^3$) functions.
* **Exactness Verification:** Proves that Simpson's rules are exact for cubic polynomials.

---

## 📐 Mathematical Formulas

### 1. Trapezoidal Rule
$$I \approx \frac{h}{2} [f(x_0) + 2 \sum_{i=1}^{n-1} f(x_i) + f(x_n)]$$

### 2. Simpson's 1/3 Rule
$$I \approx \frac{h}{3} [f(x_0) + 4 \sum_{odd} f(x_i) + 2 \sum_{even} f(x_i) + f(x_n)]$$

### 3. Simpson's 3/8 Rule
$$I \approx \frac{3h}{8} [f(x_0) + 3\sum f(x_{rest}) + 2\sum f(x_{multiples\_of\_3}) + f(x_n)]$$

---

## 🛠️ Execution Instructions

Open your terminal in the project folder and run the following commands:

```bash
# 1. Install dependencies
pip install numpy matplotlib

# 2. Run the simulation
# Note: Since main.py is in 'src', run it using:
python src/main.py
Upon execution, statistical results will be displayed in the console, and visualization graphs will be generated in the results/ directory.

📂 File Structure

Numerical-Newton-Cotes-BD71/
│
├── src/                     # 💻 Source Code Directory
│   └── main.py              # 🚀 Main Script (Run this file)
│
├── results/                 # 📊 Generated Output Graphs
│   ├── poly_visualization.png
│   ├── poly_convergence.png
│   ├── sinx_visualization.png
│   └── sinx_convergence.png
│
├── requirements.txt         # 📦 Project Dependencies
└── README.md                # 📘 Project Documentation
