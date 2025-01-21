import random
import math
import csv
from datetime import datetime

def objective_function(x):
    return x**2

def hill_climbing(start_x, step_size=0.1, max_iterations=10):
    current_x = start_x
    current_value = objective_function(current_x)
    
    # Create a list to store results
    results = [['Iteration', 'X Value', 'Function Value']]
    results.append(['Start', f"{start_x:.4f}", f"{current_value:.4f}"])
    
    for i in range(max_iterations):
        # Generate neighbors
        left_neighbor = current_x - step_size
        right_neighbor = current_x + step_size
        
        # Evaluate neighbors
        left_value = objective_function(left_neighbor)
        right_value = objective_function(right_neighbor)
        
        # Find the best neighbor
        if left_value > current_value and left_value >= right_value:
            current_x = left_neighbor
            current_value = left_value
        elif right_value > current_value:
            current_x = right_neighbor
            current_value = right_value
        else:
            # If no better neighbors, we've reached a peak
            break
            
        print(f"Iteration {i+1}: x = {current_x:.4f}, f(x) = {current_value:.4f}")
        results.append([f"Iteration {i+1}", f"{current_x:.4f}", f"{current_value:.4f}"])
    
    # Save results to CSV
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"hillclimb_results_{timestamp}.csv"
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(results)
        writer.writerow([])  # Empty row
        writer.writerow(['Final Results'])
        writer.writerow(['Best X', 'Best Value'])
        writer.writerow([f"{current_x:.4f}", f"{current_value:.4f}"])
    
    print(f"\nResults saved to {filename}")
    return current_x, current_value

def main():
    # Starting point
    start_x = random.uniform(-5, 5)
    
    print("Simple Hill Climbing Algorithm")
    print("-" * 30)
    print(f"Starting point: x = 10")
    
    # Run hill climbing
    best_x, best_value = hill_climbing(10)
    
    print("\nResults:")
    print(f"Best x found: {best_x:.4f}")
    print(f"Best value found: {best_value:.4f}")

if __name__ == "__main__":
    main()
