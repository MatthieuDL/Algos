import json

from Utils.PerformanceMetrics import analyze_functions_performance

from Sorting.MergeSort import merge_sort
from Sorting.QuickSort import quick_sort
from Searching.BinarySearch import binary_search

def main() -> None:
    functions = [
        merge_sort, 
        quick_sort,
        binary_search
        ]
    
    sizes = [int(1000*x) for x in range(1,2*10,2)]
    
    performance_data = analyze_functions_performance(functions, sizes, plot_graph=True)
    
    print(json.dumps(performance_data, indent=4))
    
if __name__ == "__main__":
    main()