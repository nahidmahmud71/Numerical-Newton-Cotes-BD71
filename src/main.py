import numpy as np
import matplotlib.pyplot as plt

# Import custom modules
from trapezoidal import trapezoidal_rule
from simpson13 import simpson_13_rule
from simpson38 import simpson_38_rule

def run_experiment(func_info):
    name = func_info['name']
    f = func_info['f']
    get_integral = func_info['integral']
    a = func_info['a']
    b = func_info['b']
    filename = func_info['filename']

    exact_val = get_integral(b) - get_integral(a)
    
    print(f"\n{'='*70}")
    print(f"ANALYSIS FOR FUNCTION: {name}")
    print(f"Range: [{a}, {b}] | Exact Value: {exact_val:.6f}")
    print(f"{'='*70}")

    print("\n--- A. SIMPLE RULES (Single Segment Application) ---")
    print(f"{'Method':<20} {'n (Segments)':<15} {'Calculated Value':<20} {'Error':<15}")
    print("-" * 70)
    

    try:
        val_trap_simple = trapezoidal_rule(f, a, b, n=1)
        err_trap = abs(val_trap_simple - exact_val)
        print(f"{'Trapezoidal':<20} {1:<15} {val_trap_simple:<20.6f} {err_trap:<15.6f}")
    except Exception as e:
        print(f"Trapezoidal Error: {e}")

    try:
        val_s13_simple = simpson_13_rule(f, a, b, n=2)
        err_s13 = abs(val_s13_simple - exact_val)
        print(f"{'Simpson 1/3':<20} {2:<15} {val_s13_simple:<20.6f} {err_s13:<15.6f}")
    except Exception as e:
        print(f"Simpson 1/3 Error: {e}")


    try:
        val_s38_simple = simpson_38_rule(f, a, b, n=3)
        err_s38 = abs(val_s38_simple - exact_val)
        print(f"{'Simpson 3/8':<20} {3:<15} {val_s38_simple:<20.6f} {err_s38:<15.6f}")
    except Exception as e:
        print(f"Simpson 3/8 Error: {e}")



    print("\n\n--- B. COMPOSITE RULES (Convergence Table) ---")
    n_values = [6, 12, 18, 24, 30, 60] 
    h_values = []
    errors = {'Trap': [], 'Simp13': [], 'Simp38': []}

    print(f"{'n':<5} {'Trapezoidal':<15} {'Simpson 1/3':<15} {'Simpson 3/8':<15}")
    print("-" * 55)

    for n in n_values:
        h = (b - a) / n
        h_values.append(h)
        
        try:
            val_trap = trapezoidal_rule(f, a, b, n)
            val_s13 = simpson_13_rule(f, a, b, n)
            val_s38 = simpson_38_rule(f, a, b, n)
            
            err_trap = abs(val_trap - exact_val)
            err_s13 = abs(val_s13 - exact_val)
            err_s38 = abs(val_s38 - exact_val)
            
            errors['Trap'].append(err_trap)
            errors['Simp13'].append(err_s13)
            errors['Simp38'].append(err_s38)
            
            print(f"{n:<5} {val_trap:<15.6f} {val_s13:<15.6f} {val_s38:<15.6f}")
            
        except ValueError as e:
            print(f"Error: {e}")

    plt.figure(figsize=(8, 5))
    plt.loglog(h_values, errors['Trap'], '-o', label='Trapezoidal')
    plt.loglog(h_values, errors['Simp13'], '-s', label="Simpson's 1/3")
    plt.loglog(h_values, errors['Simp38'], '-^', label="Simpson's 3/8")
    plt.xlabel('Step Size (h)')
    plt.ylabel('Absolute Error (Log Scale)')
    plt.title(f'Convergence Analysis: {name}')
    plt.grid(True, which="both", ls="--")
    plt.legend()
    plt.savefig(f'{filename}_convergence.png')
    print(f"[Saved] Graph: {filename}_convergence.png")

def main():
    test_cases = [
        {
            "name": "sin(x)",
            "f": lambda x: np.sin(x),
            "integral": lambda x: -np.cos(x),
            "a": 0, 
            "b": np.pi,
            "filename": "sinx"
        },
        {
            "name": "x^3 (Polynomial)",
            "f": lambda x: x**3,
            "integral": lambda x: (x**4)/4,
            "a": 0, 
            "b": 1,
            "filename": "poly"
        }
    ]

    for case in test_cases:
        run_experiment(case)

if __name__ == "__main__":
    main()
