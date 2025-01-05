import random
import time
import os
import tracemalloc

import matplotlib.pyplot as plt
import numpy as np

def create_array(x):
    return [random.randint(-1000, 1000) for _ in range(x)]

def is_search_function(func):
    search_folder = 'Searching/'
    for root, _, files in os.walk(search_folder):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as f:
                    if func.__name__ in f.read():
                        return True
    return False

def analyze_functions_performance(functions, sizes, plot_graph=True):
    performance_data = {func.__name__: {'size': [], 'time': [], 'space': []} for func in functions}

    for size in sizes:
        array = create_array(size)
        
        for func in functions:
            if is_search_function(func):
                target = random.randint(-2000, 2000)
                tracemalloc.start()
                start_time = time.time()
                func(array.copy(), target)
                end_time = time.time()
                current, peak = tracemalloc.get_traced_memory()
                tracemalloc.stop()
            else:
                tracemalloc.start()
                start_time = time.time()
                func(array.copy())
                end_time = time.time()
                current, peak = tracemalloc.get_traced_memory()
                tracemalloc.stop()
            
            performance_data[func.__name__]['time'].append(end_time - start_time)
            performance_data[func.__name__]['space'].append(peak)
            performance_data[func.__name__]['size'].append(size)

    if plot_graph:
        plot_performance(performance_data, functions)

    return performance_data

def plot_performance(performance_data, functions):
    plt.figure(figsize=(12, 12))
    for i, func in enumerate(functions):
        plt.subplot(2, len(functions), i + 1)
        sizes = performance_data[func.__name__]['size']
        times = performance_data[func.__name__]['time']
        plt.scatter(sizes, times, color='blue', label='Actual')
        
        # Fit a random line to the data
        coefficients = np.polyfit(sizes, times, 32)
        polynomial = np.poly1d(coefficients)
        fitted_line = polynomial(sizes)
        
        plt.plot(sizes, fitted_line, color='red', label='Fitted Line')
        
        plt.title(f'{func.__name__} Time Performance')
        plt.xlabel('Array Size')
        plt.ylabel('Time (seconds)')
        plt.legend()

        plt.subplot(2, len(functions), len(functions) + i + 1)
        spaces = performance_data[func.__name__]['space']
        plt.scatter(sizes, spaces, color='blue', label='Actual')
        
        # Fit a random line to the data
        coefficients = np.polyfit(sizes, spaces, 32)
        polynomial = np.poly1d(coefficients)
        fitted_line = polynomial(sizes)
        
        plt.plot(sizes, fitted_line, color='red', label='Fitted Line')
        
        plt.title(f'{func.__name__} Space Performance')
        plt.xlabel('Array Size')
        plt.ylabel('Space (bytes)')
        plt.legend()
    plt.tight_layout()
    plt.show()