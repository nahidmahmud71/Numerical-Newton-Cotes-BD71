"""
Numerical Integration Analysis (CSE 261)
Team BD71

This script implements:
1. Trapezoidal Rule
2. Simpson's 1/3 Rule
3. Simpson's 3/8 Rule
+ Adds Area Visualization and Convergence Analysis.
"""

import numpy as np
import matplotlib.pyplot as plt

# ---------------------------------------------------------
# 1. Trapezoidal Rule (Matches Report Listing 1)
# ---------------------------------------------------------
def trapezoidal_rule(f, a, b, n):
    """
    Approximates integral using Trapezoidal Rule.
    """
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f(x)
    
    # Formula: (h/2) * [y0 + 2*sum(intermediates) + yn]
    integral = (h / 2) * (y[0] + 2 * np.sum(y[1:-1]) + y[-1])
    return integral

# ---------------------------------------------------------
# 2. Simpson's 1/3 Rule (Matches Report Listing 2)
# ---------------------------------------------------------
def simpson_13_rule(f, a, b, n):
    """
    Approximates integral using Simpson's 1/3 Rule.
    Requires 'n' to be even.
    """
    if n % 2 != 0:
        raise ValueError("n must be even for Simpson's 1/3 Rule")
    
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f(x)
    
    # Formula: (h/3) * [y0 + 4*sum(odd) + 2*sum(even) + yn]
    integral = (h / 3) * (y[0] + 4 * np.sum(y[1:-1:2]) + 2 * np.sum(y[2:-2:2]) + y[-1])
    return integral

# ---------------------------------------------------------
# 3. Simpson's 3/8 Rule (Matches Report Listing 3)
# ---------------------------------------------------------
def simpson_38_rule(f, a, b, n):
    """
    Approximates integral using Simpson's 3/8 Rule.
    Requires 'n' to be a multiple of 3.
    """
    if n % 3 != 0:
        raise ValueError("n must be a multiple of 3 for Simpson's 3/8 Rule")
        
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f(x)
    
    # Iterative sum calculation (Matches Report Logic)
    sum_rest = 0
    for i in range(1, n):
        if i % 3 == 0:
            sum_rest += 2 * y[i]
        else:
            sum_rest += 3 * y[i]
            
    # Formula: (3h/8) * [y0 + sum_rest + yn]
    integral = (3 * h / 8) * (y[0] + sum_rest + y[-1])
    return integral

# ---------------------------------------------------------
# Helper: Area Visualization Plotter
# ---------------------------------------------------------
def plot_area_visualization(f, a, b, name, filename):
    """
    Generates a plot showing the function curve and the area under it.
    Visualizes the Trapezoidal approximation for n=6.
    """
    # High resolution for the smooth curve
    x_smooth = np.linspace(a, b, 200)
    y_smooth = f(x_smooth)
    
    # Low resolution for Trapezoidal segments (Visualization)
    n_viz = 6
    x_trap = np.linspace(a, b, n_viz + 1)
    y_trap = f(x_trap)
    
    plt.figure(figsize=(8, 5))
    
    # 1. Plot the actual function
    plt.plot(x_smooth, y_smooth, 'k-', linewidth=2, label=f'Exact Function: {name}')
    
    # 2. Fill the area (Exact Integration Area)
    plt.fill_between(x_smooth, y_smooth, alpha=0.2, color='blue', label='Exact Area')
    
    # 3. Show Trapezoidal Segments (The Approximation)
    plt.plot(x_trap, y_trap, 'r--o', label=f'Trapezoidal Approx (n={n_viz})', markersize=5)
    for i in range(n_viz):
        plt.vlines(x=x_trap[i], ymin=0, ymax=y_trap[i], color='red', linestyle=':', alpha=0.5)
    
    plt.title(f'Area Visualization: {name}')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # Save the plot
    save_path = f'{filename}_visualization.png'
    plt.savefig(save_path)
    print(f"Visualization saved: {save_path}")

# ---------------------------------------------------------
# Main Experiment Logic
# ---------------------------------------------------------
