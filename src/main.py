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

def run_experiment(func_info):
    name = func_info['name']
    f = func_info['f']
    get_integral = func_info['integral']
    a = func_info['a']
    b = func_info['b']
    filename = func_info['filename']

    # Exact value calculation
    exact_val = get_integral(b) - get_integral(a)

    
    print("\n" + "=" * 70)
    print(f"ANALYSIS FOR FUNCTION: {name}")
    print(f"Exact Value: {exact_val:.6f}")
    print("=" * 70)

    # --- Step 1: Generate Area Visualization ---
    print("\n[1] Generating Area Visualization Graph...")
    plot_area_visualization(f, a, b, name, filename)

  # --- Step 2: Simple Calculation Check ---
    print("\n[2] BASELINE CHECK (Simple Rules)")
    print(f"{'Method':<20} {'Segments':<15} {'Calculated':<20} {'Error':<15}")
    print("-" * 70)
    
    try:
        val = trapezoidal_rule(f, a, b, n=1)
        print(f"{'Trapezoidal':<20} {1:<15} {val:<20.6f} {abs(val - exact_val):<15.6f}")
        
        val = simpson_13_rule(f, a, b, n=2)
        print(f"{'Simpson 1/3':<20} {2:<15} {val:<20.6f} {abs(val - exact_val):<15.6f}")
        
        val = simpson_38_rule(f, a, b, n=3)
        print(f"{'Simpson 3/8':<20} {3:<15} {val:<20.6f} {abs(val - exact_val):<15.6f}")
    except Exception as e: print(e)
         # --- Step 3: Convergence Analysis (Full Table) ---
    print("\n[3] CONVERGENCE DATA TABLE (High n)")
    n_values = [6, 12, 18, 24, 30, 60] 
    h_values = []
    errors = {'Trap': [], 'Simp13': [], 'Simp38': []}

    # Print Table Header
    print(f"{'n':<5} {'Trapezoidal':<15} {'Simpson 1/3':<15} {'Simpson 3/8':<15}")
    print("-" * 55)

    for n in n_values:
        h = (b - a) / n
        h_values.append(h)
        
        try:
            v_trap = trapezoidal_rule(f, a, b, n)
            v_s13 = simpson_13_rule(f, a, b, n)
            v_s38 = simpson_38_rule(f, a, b, n)
            
            errors['Trap'].append(abs(v_trap - exact_val))
            errors['Simp13'].append(abs(v_s13 - exact_val))
            errors['Simp38'].append(abs(v_s38 - exact_val))
            
            # Print row data (Removed in previous version, now added back)
            print(f"{n:<5} {v_trap:<15.6f} {v_s13:<15.6f} {v_s38:<15.6f}")
            
        except ValueError:
            pass

    # Plotting Convergence Graph
    plt.figure(figsize=(10, 6))
    plt.loglog(h_values, errors['Trap'], '-o', label='Trapezoidal')
    plt.loglog(h_values, errors['Simp13'], '-s', label="Simpson's 1/3")
    plt.loglog(h_values, errors['Simp38'], '-^', label="Simpson's 3/8")
    
    plt.xlabel('Step Size (h)')
    plt.ylabel('Absolute Error (Log Scale)')
    plt.title(f'Convergence Analysis: {name}')
    plt.grid(True, which="both", linestyle='--')
    plt.legend()
    plt.savefig(f'{filename}_convergence.png')
    print(f"\n[Success] Convergence Graph saved: {filename}_convergence.png")
    
def main():
    test_cases = [
        {
            "name": "sin(x)",
            "f": lambda x: np.sin(x),
            "integral": lambda x: -np.cos(x),
            "a": 0, "b": np.pi, "filename": "sinx"
        },
        {
            "name": "x^3",
            "f": lambda x: x**3,
            "integral": lambda x: (x**4)/4,
            "a": 0, "b": 1, "filename": "poly"
        }
    ]
    for case in test_cases:
        run_experiment(case)

if __name__ == "__main__":
    main()
